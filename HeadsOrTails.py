""" 
This program prompts the user to play Head or Tails aganist a challenging CPU!
Author: Dee.

"""
from random import randint
from time import sleep

"""
This section gives out options and messages if you win or lose.

"""
options = ["Heads", "Tails"]
message = {
  "Won" : "Yay, you've won!",
  "Lost" : "Oops, you've lost!"
}

def decide_winner(user_guess, cpu_guess):
  print ("You have selected %s" % user_guess) 
  sleep(2)
  print ("CPU have selected %s" % cpu_guess) 
  if user_guess == options[0] and cpu_guess == options [0]:
    print (message["Won"])
  elif user_guess == options[1] and cpu_guess == options [1]:
    print (message["Won"])
  else:
    print (message["Lost"])

def play_ht():
  user_guess = input("Enter Heads or Tails: ")
  cpu_guess = options[randint(0, 1)]
  decide_winner(user_guess, cpu_guess)


play_ht()