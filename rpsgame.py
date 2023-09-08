import random
import time

poss = ("rock", "paper", "scissors")
comp = random.choice(poss)


def playrps():
    lives = 3
    while True:
        user = input("Choose rock, paper, scissors: ").lower()
        if user == "scissors" and comp == "rock":
            time.sleep(2)
            print("Computer chose: ", comp)
            print("You chose: ", user)
            lives -= 1
            print("Lives left:", lives)
            if lives == 0:
                print("You lost!")
                break
        elif user == "paper" and comp == "scissors":
            print("Computer chose: ", comp)
            print("You chose: ", user)
            lives -= 1
            print("Lives left:", lives)

        elif user == "rock" and comp == "paper":
            time.sleep(2)
            print("Computer chose: ", comp)
            print("You chose: ", user)
            lives -= 1
            print("Lives left:", lives)

        elif user == comp:
            time.sleep(2)
            print("Computer chose: ", comp)
            print("You chose: ", user)
            lives = lives
            print("Draw!, try again")

        else:
            print("Computer chose:", comp)
            print("You chose:", user)
            print("You won!")
            print("Lives left:", lives)
            break

    again = input("Do you want continue playing, Y/N:")
    if again == "y":
        playrps()
    else:
        print("Thank you for playing!")


playrps()
