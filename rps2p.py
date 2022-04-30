from time import sleep


options = ["rock", "paper", "scissors"]

def explain_game(userOne, userTwo):
  print ("User 1 has selected %s" % userOne)
  sleep(2)
  print ("User 2 has selected %s" % userTwo)
  sleep(2)
  if userOne == options[0] and userTwo == options[2]:
    print ("User One wins!")
  elif userOne == options[2] and userTwo == options[1]:
    print ("User One wins!")
  elif userOne == options[1] and userTwo == options[0]:
    print ("User One wins!")
  elif userOne == options[2] and userTwo == options[0]:
    print ("User Two wins!")
  elif userOne == options[1] and userTwo == options[2]:
    print ("User Two wins!")
  elif userOne == options[0] and userTwo == options[1]:
    print ("User Two wins!")
  elif userOne == userTwo:
    print ("Its a tie!")
  

def playrps():
  userOne = input("User One play: ")
  userTwo = input("User Two play: ")
  explain_game(userOne, userTwo)

playrps()

