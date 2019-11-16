import requests
from bs4 import BeautifulSoup

url = "http://www.zoopla.co.uk/for-sale/details/44118383?search_identifier=e31406ce57c4397baa6701b11e7cdab1"

html = requests.get(url)
soup = BeautifulSoup(html.text, "lxml")

divs = soup.find_all("div", class_="sidebar sbt")

for div in divs:
    text = div.get_text().lower()
    if(text.find("first listed") > -1):
        text = div.find("p").get_text()
        text = text.replace("\n","",10)
        text = text.strip()
        text_list = text.split()[-3:]
        text = " ".join(text_list)
        print(text)
        break
