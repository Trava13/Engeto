def change_animal(number, animal):
    if number == 1:
        return animal
    else:
        return animal + 's'

# Example usage
number_of_cows = 5
number_of_bulls = 1

print(f"{number_of_cows} {change_animal(number_of_cows, 'cow')}")
print(f"{number_of_bulls} {change_animal(number_of_bulls, 'bull')}")
