import requests
from bs4 import BeautifulSoup

def extract_news():
    url = "https://news.ycombinator.com/"
    # Ejemplo: Hacker News
    response = requests.get(url)  # Corregido: 'reponse' a 'response'
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extraer titulares como ejemplo
    titles = []
    for item in soup.select('.storylink'):
        titles.append(item.get_text())
    
    return titles  # Corregido: fuera del bucle 'for'
