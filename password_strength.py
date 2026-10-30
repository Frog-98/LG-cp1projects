#LG  Password Strength

import random

user_password = input("Create a password. Password strength is determined by capital letters, numbers, and amount of characters.")

has_capital = (char.isupper() for char in user_password)
has_number = (num() for num in user_password)
has_lower = (char.islower() for char in user_password)
s_characters = ("!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "=")
length_password = len(user_password)
while True:
    if length_password > 8:
        length_score = 1
        break
    else:
        length_score = 0
        break

while True:
    if has_capital is True:
        capital_score = 1
        break
    else:
        capital_score = 0
        break

while True:
    if has_number is True:
        number_score = 1
        break
    else:
        number_score = 0
        break

while True:
    if has_lower is True:
        lower_score = 1
        break
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

if total_score == 5:
    print("5/5, Strong Password")

elif total_score == 4:
    print("4/5")

elif total_score == 3:
    print("3/5")

elif total_score == 2:
    print("2/5")

elif total_score == 1:
    print("1/5")

else:
    print("0/5")