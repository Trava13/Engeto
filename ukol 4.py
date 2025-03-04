import json

chuckuv_slovnik = {
    "jmeno": "Chuck Norris",
    "neuspech": None,
    "kliky": "vsechny",
    "konkurence": False,
    "fanousek": "Łukasz"
}

# argument 'indent' součástí metody 'dumps'
# .. použité 4 mezery, ale hodnotu můžeš upravit
vystup_s_jsonem = json.dumps(chuckuv_slovnik, ensure_ascii=False)
print(vystup_s_jsonem)