import random

alphabet = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
special_characters = ["#", "*", "!", ".", "&", "$"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def goodPass(char):
    letters = random.sample(char, 6)
    random.shuffle(letters)
    return ''.join(letters)


def strongPass(char, special, num):
    letters = random.sample(char, 10)
    special_char = random.sample(special, 2)
    number = random.sample(num, 2)
    password_1 = letters + special_char + number
    random.shuffle(password_1)
    return ''.join(password_1)


def bestPass(char, special, num):
    letters = random.sample(char, 12)
    special_char = random.sample(special, 4)
    number = random.sample(num, 4)
    password_1 = letters + special_char + number
    random.shuffle(password_1)
    return ''.join(password_1)


def add_to_dict(dic, site, word):
    dic[site] = word
    return dic


password_dictionary = {}

print("Welcome to your password manager and generator!")

select_pass = input(
    "Which password do you want?\nSelect 1 for a good password\nSelect 2 for a strong password\nSelect 3 for the strongest and recommended password\n:")
if select_pass == "1":
    password = goodPass(alphabet)
    print("The password is:", password)
elif select_pass == "2":
    password = strongPass(alphabet, special_characters, numbers)
    print("The password is:", password)
elif select_pass == "3":
    password = bestPass(alphabet, special_characters, numbers)
    print("The password is:", password)
else:
    print("Invalid selection, choose again")

add_dict = input(
    "Would you like to add this to a dictionary?\nType Y for Yes\nType N for No\n: ")
if add_dict == "y":
    site_name = input("Which site is this password for: ")
    print(add_to_dict(password_dictionary, site_name, password))
else:
    pass
