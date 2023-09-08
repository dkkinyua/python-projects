def add_contact(name, number):
    phonebook[name] = number


def clear_contact(phonebook):
    phonebook.clear()


def remove_contact(name):
    if name in phonebook:
        del phonebook[name]
    else:
        print(f"Contact '{name}' not found in the phonebook.")


def check_phonebook(phonebook):
    return phonebook


def search_phonebook(phonebook):
    name = input("Enter the name of the contact to be searched: ")
    if name in phonebook:
        print(phonebook[name])
    else:
        pass


phonebook = {}
print("Welcome to Python Phonebook.")
print("Currently, your phonebook is empty. Add a contact to start off.")

name = input("Enter contact name: ")
number = input("Enter contact number: ")
number = int(number)
new_contact = add_contact(name, number)
print(f"The contact {name} is added successfully!")

while True:
    option = input(
        "What would you like to do? Add, clear, remove, check, search or exit phonebook: ").lower()

    if option == "add":
        name = input("Enter contact name: ")
        number = input("Enter contact number: ")
        try:
            number = int(number)
            add_contact(name, number)
            print(
                f"Contact '{name}' with phone number '{number}' added successfully!")
        except ValueError:
            print("Invalid phone number. Please enter a valid number.")

    elif option == "clear":
        clear_contact(phonebook)
        print("Phonebook cleared.")

    elif option == "remove":
        name = input("Which contact would you like to delete: ")
        remove_contact(name)
        print(
            f"The contact {name} has been deleted successfully!")

    elif option == "check":
        see_phonebook = check_phonebook(phonebook)
        print("\nPhonebook:")
        for name, number in see_phonebook.items():
            print(f"{name}: {number}")

    elif option == "exit":
        print("Thank you for using Python Phonebook!")

    elif option == "search":
        search_phonebook(phonebook)

    else:
        print("Invalid option. Please enter a valid command (add, clear, remove, check, or exit).")
