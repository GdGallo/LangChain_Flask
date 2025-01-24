import requests
from bs4 import BeautifulSoup
from database.db_config import SessionLocal
from database.models import News

def extract_news():
    url = "https://news.ycombinator.com/"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extraer los titulares usando el selector adecuado
        titles = []
        for item in soup.select('span.titleline > a'):  # Selector ajustado para obtener enlaces dentro de 'titleline'
            title = item.get_text()
            link = item['href']
            titles.append({"title": title, "url": link})
        
        # Guardar noticias en la base de datos
        db = SessionLocal()
        try: 
            for news in titles:
                # Verificar si la noticia ya existe en la base de datos
                if not db.query(News).filter_by(title=news['title']).first():
                    new_news = News(title=news['title'], url=news['url'])
                    db.add(new_news)
            db.commit()  # Confirmar todos los cambios
        except Exception as e:
            print(f"Error al guardar las noticias: {e}")
            db.rollback()  # Revertir cambios en caso de error
        finally:
            db.close()  # Cerrar la sesión

        return titles
    else:
        print(f"Error al acceder a la página: {response.status_code}")
        return []
