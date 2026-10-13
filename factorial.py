#LG, Factorial

import math

while True:
    user_number = int(input("Choose your number: "))
    if user_number>=0:
        print("")
    elif user_number < 0:
        print("Number has to be greater than or equal to zero.")
    else:
        print("Invalid number.")

    number_list =[(user_number)]
    factored_number_list = list(map(math.factorial, number_list))

    print(f"{number_list[0]}! is:")
    print(*factored_number_list)
