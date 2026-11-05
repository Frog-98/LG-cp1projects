#LG  Password Strength

import random

user_password = input("Create a password. Password strength is determined by capital letters, numbers, and amount of characters.")

s_score = 0
lower_score = 0
number_score=0
capital_score = 0
length_score = 0
has_capital = (char.isupper() for char in user_password)
has_number = (num() for num in user_password)
has_lower = (char.islower() for char in user_password)
s_characters = ("!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "=")
numbers = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
while True:
    if len(user_password) >= 8:
        length_score = 1
    break

while True:
    if has_capital is True:
        capital_score = 1
    break

while True:
    for num in user_password:
        if num in numbers:
            number_score = 1
    break

while True:
    for char in user_password:
        if char in has_lower:
            lower_score = 1
    break
  

while True:
    for char in user_password:
        if char in s_characters:
             s_score = 1
    break


total_score = length_score + capital_score + number_score + lower_score + s_score

if int(total_score) == 5:
    print("5/5, Strong Password")

if int(total_score) == 4:
    print("4/5")

if int(total_score) == 3:
    print("3/5")

if int(total_score) == 2:
    print("2/5")

if int(total_score) == 1:
    print("1/5")

else:
    print("0/5")
