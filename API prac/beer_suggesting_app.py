import json
import requests
from random import randint

food_choice = input("What are you having for dinner: ")

url = f"https://api.punkapi.com/v2/beers?food={food_choice}"

r = requests.get(url)

data = json.loads(r.text)

beer_list = []

for beer in data:
    name = beer["name"]
    tagline = beer["tagline"]
    abv = beer["abv"]

    beer_dict = {
        "name": name,
        "tagline": tagline,
        "abv": abv
    }

    beer_list.append(beer_dict)

value = randint(0, len(beer_list))

try_this = beer_list[value]

try_name = try_this["name"]
try_tagline = try_this["tagline"]
try_abv = try_this["abv"]

print(f"You should try {try_name}, {try_tagline}, with an abv of {try_abv}")
