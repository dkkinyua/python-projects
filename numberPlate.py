"""
A number plate genrator by dkkinyua. Enjoy

"""

import random
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
name = input("Enter your name: ")
print(f"Hello {name}, welcome to the number plate generator (Kenyan). It'll generate numberplates from KD* **** and not any later than this. ")


numberPlate = ""

plateLetter1 = random.choice(letters)
plateLetter2 = random.choice(letters)
plateNumber1 = random.choice(numbers)
plateNumber2 = random.choice(numbers)
plateNumber3 = random.choice(numbers)
numberPlate = "KD" + plateLetter1 + " " + plateNumber1 + \
    plateNumber2 + plateNumber3 + plateLetter2

print(f"Hi {name}, your number plate is: {numberPlate}")
