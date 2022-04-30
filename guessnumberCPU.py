"""
A guessing game by dkkinyua1.
This program prompts the user to guess a number in range 0 to 10 and if the number matches the number CPU gets, you win!
You have 10 guesses to go. Enjoy!

"""
import random
from time import sleep


def guessNumber(x):
    randomNumber = random.randint(1, x)
    guess = 0
    while guess != randomNumber:
        guess = int(input(f"Enter a number between 1 and {x}: "))
        if guess > randomNumber:
            print("Oops, too high. Try again!")
        elif guess < randomNumber:
            print("Yikes, too low. Try again!")

    print(f"Yaay, congrats. You got the number {guess} correctly!!")


def computerGuess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(
            f"Is {guess} too high (H), too low(L), or correct(c): ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f"The computer guessed {guess} correctly!!")


computerGuess(1000)
