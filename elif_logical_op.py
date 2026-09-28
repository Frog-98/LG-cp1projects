#LG, Elif and Logical Operators Notes

age = 17
liscense = True

if  age >= 18:
    print("You are an adult and can vote!")
elif age >= 15 and liscense:
    print("You can drive! But you are a minor, so go to school!")
elif age >= 15 and not liscense:
    print("You could drive. . . But you dont have the paperwork :( also go to school")
else:
    print("You are too young to drive, Go to school.")


win = True
hp = 0

if win or hp <= 0:
    print("Game Over")
    if hp > 0:
        pass
    else:
        print("You lost :(")
else:
    print("The game is still going")