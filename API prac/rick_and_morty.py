# Using the Rick and Morty API to learn and better understand API's and JSON in Python


import json
import requests

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

base_url = "https://rickandmortyapi.com/api/"

endpoint = "character"


def main_request(base_url, endpoint, x):
    r = requests.get(base_url + endpoint + f"?page=x")
    return r.json()


def get_pages(response):
    return data["info"]["pages"]


def parse_json(response):
    char_list = []
    for item in response["results"]:
        ep = len(item["episode"])
        char = {
            "ID:": item["id"],
            "Name:": item["name"],
            "Episodes in:": ep
        }
        char_list.append(char)
    return char_list


def input_data(response, user_input):
    for item in response["results"]:
        if user_input == item["name"]:
            char_info = {
                "ID:": item["id"],
                "Name:": item["name"],
                "Episodes in:": len(item["episode"]),
                "Status:": item["status"],
                "Species:": item["species"],
                "Last location:": item["location"]
            }
            return char_info


data = main_request(base_url, endpoint, 1)

is_program_finished = False

print("Welcome to Rick and Morty's program!")

while is_program_finished == False:
    gen_input = input(
        "Would you like to:\nSearch for a character info(s)\nCheck all characters(c)\nNumber of episodes(n)\nor Exit program(x):\n")
    if gen_input == "s":
        user_input = input(
            "Search for your favourite character:\n").title()
        result = input_data(data, user_input)
        print(result)
    elif gen_input == "c":
        result = parse_json(data)
        print(result)
    elif gen_input == "n":
        result = get_pages(data)
        print(result)
    elif gen_input == "x":
        is_program_finished = True
    else:
        pass
