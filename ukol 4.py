import random
print(
    "Hi there!",
    "-----------------------------------------------",
    "I've generated a random 4 digit number for you.",
    "Let's play a bulls and cows game.",
    "-----------------------------------------------",
    sep="\n"
)

def number_check(number):
    #This function check if number is corect
    return number.isdigit() and len(number) == 1
def ran_number_check(number):
    #This function check if number is corect
    number_str = str(number)
    return  len(set(number_str)) == 1
def generate_valid_number():
    while True:
        random_number = random.randint(1,9 )
        if ran_number_check(random_number):
            return random_number
def use_num():
    #User number
    user_num = input("Enter a number: ")
    print("-----------------------------------------------")
    #Checking user num
    while True:
        if number_check(user_num):
            break
        else:
            print("Invalid input")


user_num = use_num()
while True:
    ran_number = generate_valid_number()
    if user_num == str(ran_number):
        print(
            "Correct, you've guessed the right nuber",
            "-----------------------------------------------",
            "That's amazing",
            sep="\n"
        )
        break
    else:
        print(">>> ", ran_number)
        continue 

