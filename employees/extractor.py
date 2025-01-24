import requests
from bs4 import BeautifulSoup

def extract_news():
    url = "https://news.ycombinator.com/"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extraer los titulares usando el selector adecuado
        titles = []
        for item in soup.find_all('tr', class_='athing submission'):
            titles.append(item.get_text())
        
        # Verifica si los títulos se han extraído correctamente
        if titles:
            return titles
        else:
            print("No se han encontrado títulos.")
    else:
        print(f"Error al acceder a la página: {response.status_code}")

# Llamar a la función para obtener los titulares
news_titles = extract_news()
if news_titles:
    print("Titulares extraídos:")
    for title in news_titles:
        print(title)
else:
    print("No se encontraron titulares.")
