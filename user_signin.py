#LG, Username and Password

username = input("What is your username?").strip().lower()
password = input("What is your password?").strip().lower()

correct_username = "userone"
correct_password = "password"

if username == correct_username and password == correct_password:
    print(f"Welcome {username}.")
elif username == correct_username and password != correct_password:
    print("Correct username but incorrect password, try again.")
elif username != correct_username and password == correct_password:
    print("Correct password but incorrect username, try again.")
else:
    print("Incorrect username and password")



