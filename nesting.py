# LG, Nesting Notes

win = True
text = True

if win:
    if text:
        print("Hallalujah")
    else:
        print("Try Again")
else:
    print("You Failed")

names = ["Alex", "Katie", "Andrew", "Tia", "Treyson", "Xavier", "Jake"]

while True:
    for name in names:
        print(f"{name} LaRose")
    again = input("Do you need to see them again: ")
    if again.lower() == "yes":
        pass
    else:
        break

loop=range(1,10)
loop2=range(1,11)
for i in loop:
    for i in loop2:
        print(1)