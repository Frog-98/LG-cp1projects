# LG, String Methods

sentence = "The quick  brown fox jumps over the lazy dog"

fixed = sentence.replace("fox", 'wolf')

name = input("What is your name: ")

print("Hello "+name.strip().title())

print(sentence.lower())
print(sentence.upper())
print(sentence.capitalize())
print(sentence.title())
print(fixed)

letter = input("Give me a letter: ")
letter = letter[0].lower()
number_value = ord(letter)
number_value += 2
new_letter += chr(number_value)
print(f"your letter was {letter} now it is {new_letter}") 