"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Jakub Trávníček
email: jakubtravnicek@hotmail.com
"""
import random
print(
    "Hi there!",
    "-----------------------------------------------",
    "I've generated a random 4 digit number for you.",
    "Let's play a bulls and cows game.",
    "-----------------------------------------------",
    "Enter a number:",
    sep="\n"
)

def number_check(number):
    #This function check if number is corect
    return number.isdigit() and len(number) == 4 and number[0] != "0" and len(set(number)) == 4
def ran_number_check(number):
    #This function check if number is corect
    number_str = str(number)
    return  len(set(number_str)) == 4
def generate_valid_number():
    while True:
        random_number = random.randint(1000, 9999)
        if ran_number_check(random_number):
            str_random_number = str(random_number)
            return str_random_number
def use_num():
    #User number
    print("-----------------------------------------------")
    user_number = input(">>> ")
    while not number_check(user_number):
        print("Invalid input")
        user_number = input("Enter a 4-digit number: ")
    else:
        return user_number
def split(number):
    split_num = list(number)
    return split_num
def cows(num_u, num_r):
        ran_split = split(num_r)
        user_split = split(num_u)
        common_number = set(ran_split) & set(user_split)
        count_c = len(common_number)
        return count_c
def bulls(num_u, num_r):
    ran_split = split(num_r)
    user_split = split(num_u)
    bulls_c = 0
    for i in range(len(ran_split)):
        if ran_split[i] == user_split[i]:
            bulls_c += 1
    return bulls_c
def change_end_word(number, animal):
    if number == 1:
        return animal
    else:
        return animal + "s"
    
user_num = use_num()
ran_num = generate_valid_number()
count = 0

while True:

    if user_num == str(ran_num):
        print(
            "Correct, you've guessed the right nuber",
            "-----------------------------------------------",
            f"in {count} guesses!",
            "That's amazing",
            "-----------------------------------------------",
            sep="\n"
        )
        break
    else:
        count_cow = cows(user_num, ran_num)
        count_bull = bulls(user_num, ran_num)
        print(f"{count_cow} {change_end_word(count_cow, 'cow')}, {count_bull} {change_end_word(count_bull, 'bull')}")
        user_num = use_num()
        count += 1

