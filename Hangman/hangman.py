# The Hangman game.

import random
from words import word_list

# A function to be called to fetch the chosen word from words.py


def get_chosen_word():
    chosen_word = random.choice(word_list)
    return chosen_word.upper()

# A function to be called when the user selects the difficulty


def play_hangman(word):
    underscored_word = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Welcome to Hangman! Let's play!")
    print("Initial lives left: ", tries)
    print(underscored_word)
    print("\n")
    while not guessed and tries > 0:
        print(word)
        guess = input("Guess a letter or a word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(guess, "is in guessed letters.")
                guessed_letters.append(guess)
            elif guess not in word:
                print(guess, "is not in word!")
                tries = tries - 1
                guessed_letters.append(guess)
            else:
                print(f"{guess} is in word!")
                guessed_letters.append(guess)
                word_as_list = list(underscored_word)
                indices = [i for i, letter in enumerate(
                    word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                underscored_word = "".join(word_as_list)
                if "_" not in underscored_word:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("Word has already been guessed!")
                guessed_words.append(guess)
            elif guess != word:
                print(f"Word is not correct")
                tries = tries - 1
                guessed_words.append(guess)
            else:
                print("Word is correct!")
                underscored_word = word
                break
        else:
            print("Not valid, try again!")

        print("Tries left: ", tries)
        print(underscored_word)
        print("\n")
    if guessed:
        print("You guessed the word correctly!")

    else:
        print(f"The word is {word}, try better next time")


def main_function():
    word = get_chosen_word()
    play_hangman(word)
    while input("Want to play again (Y/N):") == "y":
        word = get_chosen_word()
        play_hangman(word)


if __name__ == "__main__":
    main_function()
