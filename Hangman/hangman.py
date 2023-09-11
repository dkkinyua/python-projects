# Self built hangman game, added difficulty
import random 
from words import word_list

# A function to get the random word from wowrd_list from the words.py module
def get_chosen_word():
    word = random.choice(word_list)
    return word.upper()

# A function to hide the chosen word within underscores, not to reveal the real identity
def hide_word(word):
    underscored_word = "_" * len(word)
    return underscored_word

def play_hangman():
    print("Welcome to Python Hangman!")
    guessed_letters = []
    guessed_words = []
    is_word_complete = False

    difficulty = input("Enter the difficulty you would like to play on:\nEasy(E) (Lives = 10)\nHard(H) (Lives = 7)\nor Expert(X) (Lives = 5): ").lower()
    if difficulty == "e":
        lives = 10
    elif difficulty == "h":
        lives = 7
    elif difficulty == "x":
        lives = 5



    print(f"Initial lives: {lives}\n")
    word = get_chosen_word()
    underscored_word = hide_word(word)
    print(f"Chosen word: {underscored_word}\n")

    while not is_word_complete and lives > 0:
        user_guess = input("Enter your guess, either letter or whole word: ").upper()

        #This if block check if the letter is correct or not
        if len(user_guess) == 1 and user_guess.isalpha():
            #if if block checks if the user guess is in the guessed letters list
            if user_guess in guessed_letters:
                print(f"{user_guess} is in the guessed letters!")
                guessed_letters.append(user_guess)
            #if the guess is not in the word
            elif user_guess not in word:
                print(f"{user_guess} is not in word, wrong guess. Try again!")
                lives = lives - 1
                guessed_letters.append(user_guess)
            #The guess is correct
            else:
                print(f"{user_guess} is in the word!\n")
                guessed_letters.append(user_guess)
                word_as_list = list(underscored_word)
                indices_in_list = [i for i, letter in enumerate(word) if letter == user_guess]
                for index in indices_in_list:
                    word_as_list[index] = user_guess
                underscored_word = "".join(word_as_list)
                if "_" not in underscored_word:
                    is_word_complete = True
        
        #This elif block checks if word is correct or not
        elif len(user_guess) == len(word) and user_guess.isalpha():
            if user_guess in guessed_words:
                print(f"{user_guess} is in the guessed words.")
                guessed_words.append(user_guess)
            elif user_guess != word:
                print(f"{user_guess} is not correct.")
                lives = lives - 1
                guessed_words.append(user_guess)
            else:
                underscored_word = user_guess
                is_word_complete = True       

        # This executes if the user has entered a number or anything that is not in the alphabet    
        else:
            print("Wrong Input, try again.")

        print(f"Word: {underscored_word}")
        print(f"Lives left: {lives}")

    if is_word_complete == True:
        print("Congrats, you have guessed the word corrctly!")
        
    else:
        print(f"The correct word is {word}, try better next time!")


if __name__ == "__main__":
    play_hangman()


if input("Want to try again(Y/N): ") == "y":
    play_hangman()
else:
    
    print("Okay, have a great day!")
        

