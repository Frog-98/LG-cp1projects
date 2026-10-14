#LG, Factorial

import math

break_other = False
while True:
    while True:

        try:
            user_number = int(input("Choose your number (type 9999 to quit): "))
        except:
            print("Please input an integer.")
        else:
            if user_number == 9999:
                break_other = True
                break
            if user_number>=0:
                break
            elif user_number < 0:
                print("Number has to be greater than or equal to zero.")
            else:
                print("Invalid number.")
    
    if break_other:
        break
    
    number_list =[(user_number)]
    factored_number_list = list(map(math.factorial, number_list))



    print(f"{number_list[0]}! is:")
    print(*factored_number_list)
