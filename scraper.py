import requests
from bs4 import BeautifulSoup

def scrape_headlines(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    headlines = []
    for item in soup.find_all('h2', class_='entry-title'):  # Example selector, change as per website
        headline = item.get_text()
        headlines.append(headline)
    
    return headlines
