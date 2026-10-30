#LG  Password Strength

import random

user_password = input("Create a password. Password strength is determined by capital letters, numbers, and amount of characters.")

has_capital = (char.isupper() for char in user_password)
has_number = (num() for num in user_password)
has_lower = (char() for char in user_password)
s_characters = ("!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "=")

while True:
    if user_password >= 8 and user_password <= 20:
        character_score = 1
    else:
        length_score = 0
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

while True:
    if has_lower is True:
        lower_score = 1
    else:
        lower_score = 0
        break

while True:
    for char in user_password:
        if char in s_characters:
             s_score = 1
        else:
             s_score = 0
    break


total_score = int(length_score) + int(capital_score) + int(number_score) + int(lower_score) + int(s_score)

if total_score == 3:
    print("3/3, Strong Password")

if total_score == 2:
    print("2/3")

if total_score == 1:
    print()

else:
    print("Invalid Password")