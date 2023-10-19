import functions as f

print("Welcome to the Python Area Calculator!")
user_input = input(
    "Enter a shape to calculate its area.\nSelect T for Triangle\nC for Circle\nTR for Trapezium, and\nR for Rectangle:")
if user_input == "t":
    height = int(input("Enter height: "))
    length = int(input("Enter base length: "))
    print("The area is: ", f.triangle_area(height, length))
elif user_input == "c":
    diameter = int(input("Enter diameter: "))
    print("The area is: ", f.circle_area(diameter))
elif user_input == "tr":
    a = int(input("Enter the shorter length, a: "))
    b = int(input("Enter the longer length, b: "))
    c = int(input("Enter height: "))
    print("The area is: ", f.trapezium_area(a, b, c))
elif user_input == "r":
    n1 = int(input("Enter length: "))
    n2 = int(input("Enter width / breadth: "))
    print("The area is: ", f.rectangle_area(n1, n2))
else:
    pass
