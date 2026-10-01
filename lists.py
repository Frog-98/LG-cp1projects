# LG, Lists Tuples and Sets

siblings = ["Isaac", "Pedro", "Daniel", "John", "Arthur", "Dutch", "Javier", "Charles", "Lenny"]
length = len(siblings)
print(f"My older sister is {siblings[1]}")
print(*siblings)
print(f"The youngest is {siblings[-1]}")
siblings.append("Lincoln")
siblings.insert(3, "Vienna")
siblings.extend(["Trelawny", "Jack", "Sean"])
siblings.remove("Lincoln")
siblings.pop(0)
print(*siblings)