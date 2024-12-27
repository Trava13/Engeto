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
#Defination function for counting
def counting():
    #Def variebles
    number_tittles = 0
    number_upper = 0
    number_lower = 0
    number_numeric = 0
    list_words = []
    words_lenth = []
    #Counting words
    word = TEXTS[num_select - 1].split()
    word_count = len(word)
    print(f"There are {word_count} in the selected text." )
    for word in TEXTS[num_select-1].split():
        #Counting titlecase
        if word.istitle():
            number_tittles += 1
        print(f"There are {number_tittles} titlecase words")
        #Counting Upercase words
        if word.isupper() and  word.isalpha():
            number_upper += 1
        print(f"There are {number_upper} uppercase words")
        #Conunticn lowercase words       
        if word.islower():
            number_lower += 1
        print(f"There are {number_lower} uppercase words")
        #Counting numeric strings       
        if word.isnumeric():
            number_numeric += 1
        print(f"There are {number_numeric} uppercase words")
        #Sum of all number in text
        if word.isnumeric():
            int_word = int(word)
            list_words.append(int_word)
        sum_numbers = sum(list_words, 0)
        print(f"The sum of all the numers {sum_numbers}")
        print("----------------------------------------")
        #Counting words lenth a occurences
        print("LEN|{:^16}|NR.".format("OCCURENCYS"))
        print("----------------------------------------")
        word_lenth = len(word)
        words_lenth.append(word_lenth)
        max_occu = max(words_lenth)
        for i in range(1, max_occu+1):
            count_ocu = words_lenth.count(i)
            print("{:>3}".format(i),"|{:<16}|".format("*" * count_ocu), count_ocu, sep="")
#Check username and password
if user_name in reg_user and reg_user[user_name] == user_pass:
    print("----------------------------------------")
    print(f"Welcome to the app, {user_name}")
    print("We have 3 texts to be analyzed.")
    print("----------------------------------------")
    #Selecting text
    num_select = input("Enter a number btw. 1 and 3 to select: ")
    print("----------------------------------------")
    #Function for chosing text
    if num_select.isdigit():
        num_select = int(num_select)
        if num_select in range(1, 4): 
            counting()
        else:
            print("Wrong number!")
    else:
        print("Not a number, terminating the program..")
else:
    print("unregistered user, terminating the program..")