import pandas as pd
import datetime as dt


# This is a function that adds a reservation and exports it to a CSV file
def add_reservation(reservation_list):
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    no_of_guests = input(f"Dear Mr/Mrs/Dr/Eng {last_name}, how many guests are you expecting: ")
    date_expected = input("What day are you coming: ")
    time_expected = input(f"At what time on {date_expected} will you be having dinner: ")

    restaurant_details = {
        "first_name": first_name,
        "last_name": last_name,
        "guests expected": no_of_guests,
        "date expected": date_expected,
        "time expected": time_expected,
        "time submitted": dt.datetime.now()
    }
    
    reservation_list.append(restaurant_details)  # Add the reservation dictionary to the list

    # Create a DataFrame from the list of reservations
    df = pd.DataFrame(reservation_list)

    # Export the DataFrame to a CSV file
    df.to_csv('reservations.csv', index=False)

    return reservation_list

# This is a function that displays a reservation
def display_reservation(reservation_dict):
    print("Reservation details: ")
    for key, value in reservation_dict.items():
        print(f"{key}: {value}")

# Initialize an empty list to store reservations
reservation_list = []
# Number of reservations
reservations = 10

while reservations > 0:
    print("Welcome to the Restaurant Reservation.")
    print("Here's a menu of the options:")
    print("1: Make a reservation")
    print("2: Display reservation")
    print("3: Exit program")
    
    menu = input("Enter your choice (1/2/3): ")

    if menu == "1":
        reservation_list = add_reservation(reservation_list)
        reservations -= 1
    elif menu == "2":
        if len(reservation_list) > 0:
            for reservation in reservation_list:
                display_reservation(reservation)
        else:
            print("No reservations have been made yet.")
    elif menu == "3":
        break 
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4).")



print("Number of reservations reached already.")
        





