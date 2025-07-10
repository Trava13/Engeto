import requests
from bs4 import BeautifulSoup
import csv
import sys

class Scraper:
    def __init__(self, url):
        self.base_url = url #url stránka ve formátu odkazu
        self.html_text = self.get_html(url) # kód samotné stránky
        self.soup = BeautifulSoup(self.html_text, "html.parser") #vytvoření přehledné stromové struktury
        self.detail = []
        self.data = {
            "code": [],
            "location": [],
            "registred": [],
            "envelops": [],
            "valid": []
        } # samotná data úložená ve slovníku

    # Kontrola a stažení stránky
    def get_html(self, url: str) -> str: 
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.exceptions.HTTPError as e:
            raise SystemExit(f"HTTP Error: {e}")
        except Exception as e:
            raise SystemExit(f"Other Error: {e}")

    # Najde a vrátí všechna čísla obcí
    def get_village_codes(self):
        codes = []
        table_cells = self.soup.find_all("td", class_="cislo")
        for cell in table_cells:
            codes.append(cell.text)
        return codes

    # Najde a vrátí názvy všech obcí
    def get_village_names(self):
        names = []
        table_cells = self.soup.find_all("td", class_="overflow_name")
        for cell in table_cells:
            names.append(cell.text)
        return names

    # Z hlavní stránky vytáhne všechny odkazy na detailní stránky jednotlivých obcí
    def get_detail_urls(self):
        links = []
        table_cells = self.soup.find_all("td", class_="cislo")
        for cell in table_cells:
            a_tag = cell.find("a")
            if a_tag:
                full_url = f"https://www.volby.cz/pls/ps2017nss/{a_tag['href']}"
                links.append(full_url)
        return links

    # Z každé detailní stránky vytáhne data podle zadaného HTML atributu "headers"
    def get_column_data(self, column_header, get_data_from_table):
        result = []
        urls = self.get_detail_urls()
        for detail_url in urls:
            detail_html = self.get_html(detail_url)
            detail_soup = BeautifulSoup(detail_html, "html.parser")
            td_elements = detail_soup.find_all("td", headers=column_header)
            table_elements = detail_soup.find_all("table", class_="table")

            for td in td_elements:
                cleaned_text = td.text.replace('\xa0', '')
                result.append(cleaned_text)

            if get_data_from_table:
                for table in table_elements:
                    row = table.find_all('td')
                    self.detail.append([])
                    for r in row:
                        self.detail[-1].append(r.text)
        return result

    # Hlavní metoda pro získání všech potřebných dat
    def scrape(self):
        print("Stahuji data...")
        self.data["code"] = self.get_village_codes()
        self.data["location"] = self.get_village_names()
        self.data["registred"] = self.get_column_data("sa2", False)
        self.data["envelops"] = self.get_column_data("sa3", False)
        self.data["valid"] = self.get_column_data("sa6", True)
        print("Data stažena")
        return self.data

    def save_to_csv(self, filename):
        print("Ukládání souboru...")

        # Základní názvy sloupců (hlavička CSV)
        header = ["code", "location", "registred", "envelops", "valid"]

        # Seznam všech názvů stran, které najdeme v tabulkách
        political_name = []

        # Seznam všech řádků do CSV
        all_rows = []

        # Procházíme detailní tabulky po trojicích (1 stránka = 3 tabulky)
        for i in range(0, len(self.detail), 3):
            try:
                # Získáme 2. a 3. tabulku (v 1. tabulce jsou jiné informace)
                t2 = self.detail[i + 1]
                t3 = self.detail[i + 2]

                # Pomocná funkce pro zjištění názvů stran a hlasů
                def get_name_and_votes(table):
                    names = []  # názvy stran
                    votes = []  # počet hlasů
                    index = 1   # začínáme na indexu 1 (název strany)
                    while index + 1 < len(table):
                        name = table[index].strip()
                        number = table[index + 1].strip()
                        if name:  # pokud název není prázdný
                            names.append(name)
                            votes.append(number)
                        index += 5  # přeskočíme na další stranu
                    return names, votes

                # Získáme názvy a hlasy z obou tabulek
                name2, votes2 = get_name_and_votes(t2)
                name3, votes3 = get_name_and_votes(t3)

                # Spojíme dohromady názvy a hlasy
                all_names = name2 + name3
                all_votes = votes2 + votes3

                # Přidáme nové názvy stran do hlavičky (pokud tam ještě nejsou)
                for name in all_names:
                    if name not in political_name:
                        political_name.append(name)

                # Vytvoříme jeden řádek s daty z obce
                village_index = i // 3  # protože každá obec má 3 tabulky
                row = [
                    self.data["code"][village_index],
                    self.data["location"][village_index],
                    self.data["registred"][village_index],
                    self.data["envelops"][village_index],
                    self.data["valid"][village_index]
                ]

                # Vytvoříme slovník: název strany → hlasy
                votes = dict(zip(all_names, all_votes))

                # Přidáme hlasy ke každé straně v pevném pořadí
                for pol_name in political_name:
                    row.append(votes.get(pol_name, ""))  # pokud strana chybí, přidá se prázdně

                # Přidáme řádek do seznamu
                all_rows.append(row)

            except IndexError:
                print(f"Chyba při zpracování dat pro záznam č. {i // 3}")
                continue

        # Spojíme základní hlavičku + názvy stran
        complete_header = header + political_name

        # Uložíme do CSV
        with open(filename, mode="w", newline="", encoding="cp1250") as soubor:
            writer = csv.writer(soubor, delimiter=";")
            writer.writerow(complete_header)   # první řádek – hlavička
            writer.writerows(all_rows)  # ostatní řádky – data

        print(f"Soubor {filename} byl úspěšně uložen.")


# Hlavní část programu
if __name__ == "__main__":
    """
    if len(sys.argv) != 3:
        print("Použití: python main.py <URL> <název_souboru.csv>")
        sys.exit(1)

    input_url = sys.argv[1]
    scraper = Scraper(input_url)
    scraper.scrape()
    scraper.save_to_csv("vysledky.csv")
    """

    input_url = "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101"
    scraper = Scraper(input_url)
    scraper.scrape()
    scraper.save_to_csv("vysledky.csv")