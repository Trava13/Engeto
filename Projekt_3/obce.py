from requests import get
from bs4 import BeautifulSoup as bs
url = "https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=11&xobec=592897&xvyber=6206"

html = get(url)
split_html = bs(html.text, features="html.parser")
td_split = split_html.find_all("td", {"headers": "sa2"})
voters = [td.text for td in td_split]
print(voters)
html = get(url)
split_html = bs(html.text, features="html.parser")
td_split = split_html.find_all("td", {"headers": "sa3"})
envelope = [td.text for td in td_split]
print(envelope)
html = get(url)
split_html = bs(html.text, features="html.parser")
td_split = split_html.find_all("td", {"headers": "sa6"})
votes = [td.text for td in td_split]
print(votes)
#------------------------------------------------------------------
#implementovano

html = get(url)
split_html = bs(html.text, features="html.parser")
td_split = split_html.find_all("td", {"headers": "t1sa1 t1sb2"})
parts = [td.text for td in td_split]
print(parts)
html = get(url)
split_html = bs(html.text, features="html.parser")
td_split = split_html.find_all("td", {"headers": "t1sa2 t1sb3"})
vote_parts = [td.text for td in td_split]
print(vote_parts)