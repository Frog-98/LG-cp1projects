#Lincoln Girot, Pet Rock

import random
import time

print('Welcome to pet rock! Type "feed" to feed your pet rock! Type "pet" to pet your pet rock, and type "wash" yuro wash your pet rock!')

start_time = time.time()
last_fed_time = time.time()
last_pet_time = time.time()
last_wash_time = time.time()

while True:
    current_time = time.time()

    if current_time - last_fed_time > 15:
        print("\n Oh no! Your pet rock has starved.")
        break

    if current_time - last_pet_time > 30:
        print("\n Oh no! Your pet rock died of depression from not being pet.")
        break

    if current_time - last_wash_time > 60:
        print("\n Oh no! Your pet rock has died of sickness from not being washed.")
        break

    if random.random() < 0.007:
        print("\n Oh no! A seagull stole your pet rock!")
        break

    if random.random() < 0.001:
        print("\n Oh no! Your pet rock has died of cancer!")
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
    else:
        print("Your pet rock has died.")
        break

end_time = time.time()
total_time_alive = round(end_time - start_time, 1)

print(f"\n Your pet rock has died. It survived for {total_time_alive} seconds.")


