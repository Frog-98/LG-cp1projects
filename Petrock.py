#Lincoln Girot, Pet Rock

import random
import time

print('Welcome to pet rock! Type "feed" to feed your pet rock! Type "pet" to pet your pet rock, type "wash" to wash your pet rock and type "sunscreen" to put suncreen on your pet rock! ')

start_time = time.time()
last_fed_time = time.time()
last_pet_time = time.time()
last_wash_time = time.time()
last_sunscreen_time = time.time()

while True:
    current_time = time.time()

    if current_time - last_fed_time > 10:
        print("\n Oh no! Your pet rock has starved.")
        break

    if current_time - last_pet_time > 15:
        print("\n Oh no! Your pet rock died of depression from not being pet.")
        break

    if current_time - last_wash_time > 20:
        print("\n Oh no! Your pet rock has died of sickness from not being washed.")
        break

    if current_time - last_sunscreen_time > 30:
            print("\n Oh no! Your pet rock has died of sunburn!")
            break

    if random.random() < 0.01:
        print("\n Oh no! A seagull stole your pet rock!")
        break

    if random.random() < 0.005:
        print("\n Oh no! Your pet rock has died of cancer!")
        break

    if random.random() < 0.001:
        print("\n Oh no! Your pet rock spontaneously combusted!")
        break

    if random.random() < 0.001:
            print("\n Oh no! Your pet rock was drafted into World War 3!")
            break

    if random.random() < 0.0005:
                print("\n Oh no! Your pet rock was killed in a firery 4 car car crash on the freeway after attempting to flee in a high speed chase after recieving a $30 parking ticket!")
                break
    


    user_input = input("\nWhat would you like to do? ").lower().strip()


    if user_input == "feed":
        print("Pet Rock Has Been Fed!")
        last_fed_time = time.time()
    elif user_input == "pet":
        print("Pet rock has been pet!")
        last_pet_time = time.time()
    elif user_input == "wash":
        print("You pet rock has been washed!")
        last_wash_time = time.time()
    elif user_input == "sunscreen":
        print("Your pet rock has been given sunscreen!")
        last_sunscreen_time = time.time()
    else:
        print("Your pet rock has died.")
        break

end_time = time.time()
total_time_alive = round(end_time - start_time, 1)

print(f"\n Your pet rock has died. It survived for {total_time_alive} seconds.")


