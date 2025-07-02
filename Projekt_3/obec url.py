from requests import get
from bs4 import BeautifulSoup as bs

url_okres = "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6206"

html = get(url_okres)
split_html = bs(html.text, features="html.parser")
td_split = split_html.find_all("td", {"class": "cislo"})
path = []

for td in td_split:
    a_tag = td.find('a')
    if a_tag:
        path.append(a_tag['href'])

for p in path:
    odkaz = f"https://www.volby.cz/pls/ps2017nss/{p}"
    print(odkaz)

    
#ipmplementovano