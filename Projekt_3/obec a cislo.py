from requests import get
from bs4 import BeautifulSoup as bs

url_okres = "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6206"


html = get(url_okres)
split_html = bs(html.text, features="html.parser")
td_split = split_html.find_all("td", {"class": "overflow_name"})
cities = [td.text for td in td_split]
print(cities)
td_split_number = split_html.find_all("td", {"class": "cislo"})
numbers =  [td_number.text for td_number in td_split_number]
print(numbers)
