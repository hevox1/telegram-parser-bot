import requests
from bs4 import BeautifulSoup

url = "https://example.com/product"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

price_block = soup.find("span", class_="price")
price = price_block.get_text(strip=True)

print('текущая цена: ', price)

