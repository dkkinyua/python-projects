"""
This program shows and lets the user shop in a store.
Author: Dee.

"""
from math import *

groceries = {
  "Milk" : 50,
  "Eggs" : 15,
  "Cucumber" : 20,
  "Tomatoes" : 50,
  "Spring Onions": 30,
  "Red Onions" : 20,
  "Garlic" : 30,
}

stock = {
  "Milk" : 70,
  "Eggs" : 222,
  "Cucumber" : 143,
  "Tomatoes" : 279,
  "Spring Onions": 133,
  "Red Onions" : 112,
  "Garlic" : 91
}

total_money_earned = 0
for item in groceries:
  