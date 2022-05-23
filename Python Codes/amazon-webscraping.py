import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1"
PRODUCT_URL='https://www.amazon.in/'
Headers = {
    'Accept-Language':"en-US,en;q=0.9",
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
}

response = requests.get(url=URL, headers=Headers)
amazon_web_page = response.text

soup = BeautifulSoup(amazon_web_page, "html.parser")

# links= soup.select(selector='.s-search-results h2 a.a-link-normal')
links = soup.find_all('div', {'class': 's-result-item', 'data-component-type': 's-search-result'})

print(len(links))
for link in links:
    try:
        print(f"{PRODUCT_URL}{link.a.get('href')}")
        print(link.h2.text)
        print(link.find('span', {'class': 'a-offscreen'}).get_text())
        print(link.find('i', {'class':'a-icon'}).get_text())
        print(link.find('span', {'class':'a-size-base'}).get_text())
    except AttributeError:
        continue
