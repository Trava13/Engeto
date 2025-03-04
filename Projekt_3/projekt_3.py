"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie

author: Jakub Trávníček
email: jakubtravnicek@hotmail.com
"""
from requests import get
from bs4 import BeautifulSoup as bs

clanky_2021 = "https://cs.wikipedia.org/wiki/Wikipedie:%C4%8Cl%C3%A1nek_t%C3%BDdne/2021"

odpoved = get(clanky_2021)

rozdelene_html = bs(odpoved.text, features="html.parser")

vsechny_a_tagy = rozdelene_html.find_all("a", {"class": "mw-file-description"})

# projdi všechny A tagy ..
# .. vypiš obsah klíče TITLE
for a_tag in vsechny_a_tagy:
    print(a_tag.attrs.get("title", "Chybí klíč 'title'"))
