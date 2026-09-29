#LG, Letter Grade

grade = float(input("What is your grade percentage?"))

if grade >= 90 and grade <= 100:
    print(f"Your grade is a {grade} which is an A")
elif grade >= 80 and grade <= 89:
    print(f"Your grade is a {grade} which is a B")
elif grade >= 70 and grade <= 79:
    print(f"Your grade is a {grade} which is a C")
elif grade >= 60 and grade <= 69:
    print(f"Your grade is a {grade} which is a D")
elif grade >= 0 and grade <= 59:
    print(f"Your grade is a {grade} which is a F")
else:
    print("Not a valid percentage, try again")
