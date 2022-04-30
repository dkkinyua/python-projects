""" 
    A mad libs game by dkkinyua1. Enjoy! Write down an adjective, food in plural, verb, saying, noun, foods in plural, color, something you would ride in, animal and a person.
    Lesson learnt: string concantentation & input

 """

from time import sleep

# Madlib 1

userName = input("What is your name?: ")
sleep(2)
userInput = input(
    "Well Hello" + " " + userName + " " + ", choose a madlib. Type (T) for a taco madlib or (J) for a jobs madlib: " .format(userName)).lower()

if userInput == "t":
    adj = input("Enter an adjective: ")
    foods_1 = input("Enter food (in plural): ")
    verb = input("Enter an verb: ")
    saying = input("Enter a saying: ")
    noun = input("Enter a noun: ")
    food_2 = input("Enter food (in plural): ")
    color = input("Enter a color: ")
    ride = input("Enter sth you would ride in: ")
    animal = input("Enter an animal: ")
    person = input("Enter a person: ")

    print("Here's a madlib about tacos!")
    sleep(2)
    print("Today i went to my favorite Taco Stand called the " + adj + animal + ". Unlike most food stands, they cook and prepare the food in a " + ride + " while you " + verb + " The best thing on the menu is the " + color + noun +
          ". Instead of ground beef they fill up the taco with " + food_2 + ", cheese and top it off with with a salsa made from " + foods_1 + "If that doesn't make your mouth water, then it's just as " + person + " always says: " + saying + ".")

elif userInput == "j":
    occupation = input("Enter an occupation: ")
    noun1 = input("Enter a noun: ")
    adj1 = input("Enter an adjective: ")
    noun2 = input("Enter a noun: ")
    verb1 = input("Enter a verb: ")
    adj2 = input("Enter an adjective: ")
    noun3 = input("Enter a noun: ")
    verb2 = input("Enter a verb: ")
    noun4 = input("Enter a noun: ")
    verb3 = input("Enter a verb: ")
    noun5 = input("Enter a noun: ")
    verb4 = input("Enter a verb: ")

    print("Here is a madlib about jobs!")
    sleep(2)
    print("Today" + occupation + "named" + noun5 + "came to our school to talk to us about her job. She said the most important skill you need to know to do her job is to be able to" + verb4 + "around (a)" + adj1 + noun4 + ". She said it was easy for her to learn her job because she loved to" +
          verb1 + "when she was my age--and that helps a lot! If you're considering her profession, I hope you can be near (a)" + adj2 + noun1 + ". That's very important! If you get too distracted in that situation you won't be able to sleep next to(a) engineer!")
