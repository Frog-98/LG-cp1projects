#Lincoln Girot, Escape Room

print("You are trapped in an escape room with a 4 digit passowrd on the door, find the passowrd to escape!")
print("There is a painting, a lamp, a photograph, a paper, a plant, and a key.")

while True:
    action = input("Type [Investigate (OBJECT)] to investigate any of the objects. Type [Type Code] to try to type the code ").lower().strip()
    if action == "type code".lower().strip():
        type_code = input("What is the code? ")
        if type_code == "8957".strip():
            print("You escaped the room!")
            break
        else:
            print("Incorrect password, maybe try looking at the objects around the room for clues.")
    elif action == "investigate lamp".lower().strip():
        print("You look at the bottom of the lamp and see that it says (1: 8)")
    elif action == "investigate photograph".lower().strip():
        print("You turn around the photograph to see that written on the back it says (3: 5)")
    elif action == "investigate Painting".lower().strip():
        print("You look closer at the painting to see that in tiny letters it says (4: 7)")
    elif action == "investigate paper".lower().strip():
        print("You pick up the paper and see that it says (2: 9)")
    elif action == "investigate plant".lower().strip():
        print("It doesn't look like there are any clues on this plant.")
    elif action == "investgate key".lower().strip():
        print("It looks like the door needs a passcode, not a key.")
    else:
        print("Invalid command, try again.")

