"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jakub Travnicek
email: travnicekjakub@hotmail.com
"""
#Text to be analyzed
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
#Reg users
reg_user = {
    "bob": "123", 
    "ann": "pass123", 
    "mike": "password123", 
    "liz": "pass123" 
}
#Sign in
user_name = input("Username: ")
user_pass = input("Password: ")
#Check username and password
if user_name in reg_user and reg_user[user_name] == user_pass:
    print("Welcome to the app,", user_name)
    print("We have 3 texts to be analyzed.")
    num_select = int(input("Enter a number btw. 1 and 3 to select:"))
    
    if num_select is 1:
        print(TEXTS[num_select-1])
    elif num_select is 2:
        print(TEXTS[num_select-1])
    elif num_select is 3:
        print(TEXTS[num_select-1])
    else:
            print("Wrong number!")
else:
    print("unregistered user, terminating the program..")