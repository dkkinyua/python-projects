import pandas as pd

#Read the dataset
#df = pd.read_csv("Pandas/MOCK_DATA (1).csv")

"""
max_amount_shopped = df["amount shopped"].max()
max_items_shopped = df["cart"].max()

print("Max amount shopped: ", max_amount_shopped)
print("Max items shopped: ", max_items_shopped)
head = df.head(20)
print(head)
try:
    average_spend = df["amount shopped"].mean()
    print("Average amount shopped: ", average_spend)
except TypeError:
    print("Raise TypeError, because of the dollar sign, we can't find the average.")

describe = df.describe()
print(describe)
"""

person_data = {
    "first_name": ["John", "Maria"],
    "last_name": ["Doe", "Baker"],
    "email": ["johndoe@fake.com", "maria@fake.com"],
    "address": ["1 Red St, 10001 NY", "na"]
}
def add_info():
    person_first_name = input("Enter first name: ")
    person_last_name = input("Enter last name: ")
    person_email = input("Enter email address: ")
    person_address = input("Enter address: ")

    person_data["first_name"].append(person_first_name)
    person_data["last_name"].append(person_last_name)
    person_data["email"].append(person_email)
    person_data["address"].append(person_address)
    

add_info()
while True:
    if input("Want to add more info: ") == "y":
        add_info()
    else:
        break 




try:
    df = pd.DataFrame(person_data)
    print(df)
except ValueError:
    print("raise ValueError, check code and try again")

if input("Do you want to write this back to a .csv file: ") == "y":
    df.to_csv("person's data.csv")
else:
    print("Thank you.")