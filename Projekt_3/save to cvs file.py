import requests
from bs4 import BeautifulSoup as bs
import sys
import csv

def url_check(url: str) -> str:
    try:
        html = requests.get(url)
        # Check if the request was successful (status code 200)
        html.raise_for_status()  # This will raise an HTTPError for bad requests
        return html.text
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except Exception as err:
        return f"Other error occurred: {err}"
def vil_num(url: str) -> list:
    html = requests.get(url)
    split_html = bs(html.text, features="html.parser")
    td_split = split_html.find_all("td", {"class": "overflow_name"})
    village = [td.text for td in td_split]
    return village
def vil_name(url: str) -> list:
    html = requests.get(url)
    split_html = bs(html.text, features="html.parser")
    td_split = split_html.find_all("td", {"class": "cislo"})
    numbers =  [td.text for td in td_split]
    return numbers
def make_dictonary():
    dict_cv = {
        "code": [],
        "location": [],
        "registred": [],
        "envelops": [],
        "valid": []
    }
    village = vil_num(url)
    numbers = vil_name(url)
    voters = clean_list(registred, url)
    envelope = clean_list(envelopes, url)
    valids = clean_list(valid, url)
    dict_cv["code"].extend(numbers)
    dict_cv["location"].extend(village)
    dict_cv["registred"].extend(voters)
    dict_cv["envelops"].extend(envelope)
    dict_cv["valid"].extend(valids)
    return dict_cv
def list_url_vil(url):
    html = requests.get(url)
    split_html = bs(html.text, features="html.parser")
    td_split = split_html.find_all("td", {"class": "cislo"})
    paths = []
    list_urls = []
    for td in td_split:
        a_tag = td.find('a')
        if a_tag:
            paths.append(a_tag['href'])

    for path in paths:
        urls = f"https://www.volby.cz/pls/ps2017nss/{path}"
        list_urls.append(urls)     
    return list_urls
def registred(url):
    list_urls = list_url_vil(url)
    list_voters = []
    for url_vil in list_urls:
        html = requests.get(url_vil)
        split_html = bs(html.text, features="html.parser")
        td_split = split_html.find_all("td", {"headers": "sa2"})
        voters = []
        for td in td_split:
            voters.append(td.text)
        list_voters.extend(voters)
    return list_voters
def envelopes(url):
    list_urls = list_url_vil(url)
    list_voters = []
    for url_vil in list_urls:
        html = requests.get(url_vil)
        split_html = bs(html.text, features="html.parser")
        td_split = split_html.find_all("td", {"headers": "sa3"})
        voters = []
        for td in td_split:
            voters.append(td.text)
        list_voters.extend(voters)
    return list_voters
def valid(url):
    list_urls = list_url_vil(url)
    list_voters = []
    for url_vil in list_urls:
        html = requests.get(url_vil)
        split_html = bs(html.text, features="html.parser")
        td_split = split_html.find_all("td", {"headers": "sa6"})
        voters = []
        for td in td_split:
            voters.append(td.text)
        list_voters.extend(voters)
    return list_voters
def clean_list(fun, url):
    list_voters = fun(url)
    return [space.replace('\xa0', '') for space in list_voters]
    

#Main function
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)
    url = sys.argv[1]
    html_data = url_check(url)
    dict_to_cv = make_dictonary()
    print(dict_to_cv)



    