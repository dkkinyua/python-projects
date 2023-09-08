"""
This is a guessing game based on difficulty. Guess a number and enjoy

"""

import random


def playgame():

    diff = input(
        "Choose the difficulty, Easy(e), Normal(n), Novice(v), Expert(x): ").lower()
    if diff == "e":
        guess = random.randint(1, 10)
        lives = 3
    elif diff == "n":
        guess = random.randint(1, 50)
        lives = 5
    elif diff == "v":
        guess = random.randint(1, 100)
        lives = 7
    elif diff == "x":
        guess = random.randint(1, 1000)
        lives = 10
    else:
        print("Wrong entry.")

    while True:
        number = int(input("Guess a number: "))
        lives = lives - 1
        if number < guess:

    while True:
        user = input("Choose rock, paper, scissors: ").lower()
        print("Guess higher")
        print("Lives left:", lives)
        if lives == 0:
            print("Game over, you ran out of lives. The correct guess was:", guess)
            break
        elif number > guess:
            print("Guess lower")
            print("Lives left:", lives)

        else:
            print("You won!")
            print("Lives left:", lives)
            break

    again = input("Do you want to continue playing, Y/N: ").lower()
    if again == "y":
        playgame()
    else:
        print("Thanks for playing.")


playgame()
