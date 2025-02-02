"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Jakub Trávníček
email: jakubtravnicek@hotmail.com
"""
import random
#Set functions
def number_check(number):
    """
    This function verify number are digit, long 4 charachters, not strat with 0 and all for number are uniq
    Example:
    Corect input: 
    1234, 2579, and so on
    Incorect input:
    1224 due to duplicit number 2
    hgfj character are not digit
    12 to short
    123456 to long
    0254 stra with 0
    """
    return number.isdigit() and len(number) == 4 and number[0] != "0" and len(set(number)) == 4
def ran_number_check(number):
    """
    This function verify 4 digit numbers are not duplicit
    Example:
    Corecet: 1234 
    Incorect: 2334  
    """
    number_str = str(number)
    return  len(set(number_str)) == 4
def generate_valid_number():
    while True:
        """
        This function genareta number between 1000 and 9999
        """
        random_number = random.randint(1000, 9999)
        if ran_number_check(random_number):
            str_random_number = str(random_number)
            return str_random_number
def use_num():
    """
    This function takeking input from user and validate it. For validating function use function number_check
    """
    print("-----------------------------------------------")
    user_number = input(">>> ")
    while not number_check(user_number):
        print("Invalid input")
        user_number = input("Enter a 4-digit number: ")
    else:
        return user_number
def split(number):
    """
    This function split input to the characters
    Example:
    if input 1234 then output is list[1,2,3,4]
    """
    split_num = list(number)
    return split_num
def cows(num_u, num_r):
    """
    This function comparing two lists if ther is a matche. Next sum the mathes in thi list a return them like output
    """
    ran_split = split(num_r)
    user_split = split(num_u)
    common_number = set(ran_split) & set(user_split)
    count_c = len(common_number)
    return count_c
def bulls(num_u, num_r):
    """
    This function comparing two lists and looking for match on same position.
    Example:
    List 1 [1,2,3,4]
    List 2 [5,2,6,4]
    Function find mataxh on first pozion a last. Output will be two.
    """
    ran_split = split(num_r)
    user_split = split(num_u)
    bulls_c = 0
    for i in range(len(ran_split)):
        if ran_split[i] == user_split[i]:
            bulls_c += 1
    return bulls_c
def change_end_word(number, word):
    """
    This function add "s" when is word have more then 1 occurencis
    """
    if number == 1:
        return word
    else:
        return word + "s"
#Wellcome message
print(
    "Hi there!",
    "-----------------------------------------------",
    "I've generated a random 4 digit number for you.",
    "Let's play a bulls and cows game.",
    "-----------------------------------------------",
    "Enter a number:",
    sep="\n"
)
#Call user input and verify it  
user_num = use_num()
#Generate random number and verify it
ran_num = generate_valid_number()
#Here is torete number fo wrong guesses guesses
count = 0
#Function which will repate until you find the random number
while True:
    #When you number function stop and print the text
    if user_num == str(ran_num):
        print(
            "Correct, you've guessed the right nuber",
            f"in {count} guesses!",
            "-----------------------------------------------",
            "That's amazing",
            "-----------------------------------------------",
            sep="\n"
        )
        break 
    else:
        #Here we calling def function which count cows adn bulls
        count_cow = cows(user_num, ran_num)
        count_bull = bulls(user_num, ran_num)
        print(f"{count_bull} {change_end_word(count_bull, 'bull')}, {count_cow} {change_end_word(count_cow, 'cow')}")
        #Caling user input
        user_num = use_num()
        #For every wrong guesse add 1 to count
        count += 1