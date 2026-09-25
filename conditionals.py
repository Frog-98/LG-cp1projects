# LG Conditional Notes
grade = 64

if grade >= 90:
    print("You have an A.")
elif grade >= 70:
    print("You are passing!")
else:
    print("You are not passing")
    print("Do you need to retake a quiz? Or do you need to submit a missing assignment?")


username = input("What is your username: ")

if bool(username):
    print("You didnt type it in.")
elif username == "LaRose":
    print("You are the teacher!")
else:
    print("You are a student!")

raining = False

if raining:
    print("Bring and umbrella")
else:
    print("Wear Sunscreen")