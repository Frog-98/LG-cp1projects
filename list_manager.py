#LG, List Manager

shopping_list=["Egss", "Milk"]
while True:
    #get their input about adding, removing, printing, or exiting
    action = input("Choose a command [Add, Print, Remove, Exit] ").lower().strip()
    if action=="add":
        add_item = input("What item do you want to add to the list? ").strip().lower()
        shopping_list.append(add_item)
    elif action == "print":
        print(*shopping_list)
    elif action == "remove":
        remove_item = input("What item do you want to remove?").strip()
        try:
            shopping_list.remove(remove_item)
        except:
            print("Invalid Item")
            continue
    elif action == "exit":
        break
    else: print("Invalid Command")
