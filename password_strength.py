#LG  Password Strength

import random

user_password = input("Create a password. Password strength is determined by capital letters, numbers, and amount of characters.")

has_capital = any(char.isupper() for char in user_password)
has_number = any(num() for num in user_password)


while True:
    if user_password > 8 and user_password < 20:
        character_score = 1
    else:
        character_score = 0
        break

while True:
    if has_capital is True:
        capital_score = 1
    else:
        capital_score = 0
        break

while True:
    if has_number is True:
        number_score = 1
    else:
        number_score = 0
        break


total_score = int(character_score) + int(capital_score) + int(number_score) + int

if total_score == 3:
    print("3/3, Strong Password")

if total_score == 2:
    print("2/3")

if total_score == 1:
    print()

else:
    print("Invalid Password")