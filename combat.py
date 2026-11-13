#LG, Combat

import random

Player_health = (100)
Player_moves = ("quick attack", "static shock", "wave")
Player_special_moves = ("lightning", "hyperbeam")
Enemy_health = (50)
Enemy_moves = ("quick attack", "scratch", "tackle")

print("A wild mousey has appeared! choose a pokeguy to fight it!")
print("Available Pokemon: Chickapu, Turtley, Lizardo, Plantasaurus")
player_monsters = ("chickapu", "turtley", "lizardo", "plantasaurus")

while True:
    player_monster = input("Which Pokeguy do you want?").lower().strip()
    if player_monster in player_monsters:
        print("Go, " + (player_monster) + "!")
    