""" 
This program calculates the area of different shapes e.g. circle, triangle
Author: Dee.

"""
from math import *
from time import sleep

print ("Welcome to the Area Calculator!")
print ("Enter a shape to get its area.")
user_input = input("Choose, C for Circle, T for Triangle, R for Rectangle: ")
if user_input == "C":
  radius = int(input("Enter radius: "))
  pi = 3.1428
  area = pi * radius ** 2
  print ("The area of the circle is %d" % area)
elif user_input == "T":
  base = int(input("Enter base: "))
  height = int(input("Enter height: "))
  area = 0.5 * base * height
  print ("The area of the triangle is %d" % area)
elif user_input == "R":
  length = int(input("Enter Length: "))
  width = int(input("Enter Width: "))
  area = length * width
  print ("The area of the rectangle is %d" % area)
