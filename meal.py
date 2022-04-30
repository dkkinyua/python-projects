print ("Welcome to Dee's Restaurant!")
print ("How may we be of service?")
option = input("Enter a meal: ")
tax = 7 / 100
tip = 10 / 100
if option == "Chicken Tikka".lower():
  tikka = 15.00
  total = tikka + tikka + tax * tip
  print ("Your total cost for the meal is %d" % total)
elif option == "Chocolate Smoothie".lower():
  choc = 25.00
  total = choc + choc + tax * tip
  print ("Your total cost for the meal is %d" % total)
elif option == "French Fries".lower():
  fries = 45.00
  total = fries + fries + tax * tip
  print ("Your total cost for the meal is %d" % total)
elif option == "Coffee and Toast".lower():
  toast = 7.50
  total = toast + toast + tax * tip
  print ("Your total cost for the meal is %d" % total)
else:
  print("We don't serve that here, am sorry. Check the menu for meals.")


