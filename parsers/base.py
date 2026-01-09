import requests
from bs4 import BeautifulSoup


# # url = "https://chatgpt.com/"
# url = "https://example.com"
#
# response = requests.get(url)
# html = response.text
#
# soup = BeautifulSoup(html, "html.parser")
#
# h1_text = soup.find("p").text
#
# paragraphs = soup.find_all("p")
# for p in paragraphs:
#     print(p.text)
#
# print("_______",h1_text)



url = "https://www.idealo.de/preisvergleich/ProductCategory/16455F2087885-4978814.html?q=brillengestell+von+ray+ban&msclkid=7d14fbf492f91b8bf2b392ab0d5149c3&utm_source=bing&utm_medium=cpc&utm_campaign=Brillen_16455&utm_term=brillengestell%20von%20ray%20ban&utm_content=16455_00660"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

code_block = soup.find("div", class_="sr-detailedPriceInfo__pricePrefix_cwfO5 sr-de_DE__oyjw")

print(code_block.text.strip())
# tag = soup.find("h1")
#
# if tag:
#     print(tag.text)
# else:
#     print("tag not found")

# print("FULL TEXT:\n", soup.text) # весь текст страницы
# print("\n\n\n\nTITLES:\n",soup.title.text) # <title>





