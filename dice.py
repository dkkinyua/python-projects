"""  
This is a program that prompts the user to play a dice game and determines the winner either the user or the computer
Author: Dee

"""
from random import randint
from time import sleep
user_input = input("Enter your name: ")
sleep(1)
def get_user_guess():
  guess = int(input("Make a guess: "))
  return guess
  
def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print ("The maximum possible value is: %d" % max_val)
  guess = get_user_guess()
  if guess > max_val:
    print ("%d is invalid!" % guess)
  else:
    print ("Rolling...")
    sleep(2)
    print ("The first roll is... %d" % first_roll)
    sleep(1)
    print ("The second roll is... %d" % second_roll)
    sleep(1)
    total_roll = first_roll + second_roll
    print ("The total roll is %d" % total_roll)
    print ("Result...")
    sleep(1)
    if guess == total_roll:
      print ("Congratulations, you have won!")
    else:
      print ("You have lost!")

      
roll_dice(6)
  
