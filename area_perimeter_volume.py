# A area, volume, perimeter calculator using classes, and use of OOP

import math

# This class is for calculating the area of different objects


class Area:
    def __init__(self, l, w):
        self.length = float(l)
        self.width = float(w)

    def calculate_area(self, user_input):
        if user_input == "c":
            area = math.pi * self.length * self.length
            return area
        elif user_input == "r":
            area = self.length * self.width
            return area
        elif user_input == "s":
            area = self.length * self.width
            return area
        elif user_input == "t":
            area = 0.5 * self.length * self.width  # take width as height
            return area


# This class is for calculating the perimeter of different objects
class Perimeter:
    def __init__(self, l, w):
        self.length = float(l)
        self.width = float(w)

    def calculate_perimeter(self, user_input):
        if user_input == "c":
            perimeter = 2 * math.pi * self.length
            return perimeter
        elif user_input == "r":
            perimeter = 2 * (self.length) + 2 * (self.width)
            return perimeter
        elif user_input == "s":
            perimeter = 2 * (self.length + self.width)
            return perimeter
        elif user_input == "t":
            perimeter = 3 * (self.length)  # take width as height
            return perimeter


# This class is for calculating the volume of different shapes
class Volume:
    def __init__(self, a, h):
        self.area = float(a)
        self.height = float(h)

    def calculate_volume(self, user_input, area_input):
        volume = self.area * self.height
        return volume


print("Welcome to the Python area, perimeter, and volume calculator!")


def main_program():
    while True:
        choose_calculation = input(
            "Choose to calculate\nArea(a)\nPerimeter(p)\nVolume(v) or to\nExit program(x):")

        # This "if" is if the user selects to calculate area
        if choose_calculation == "a":
            user_input = input(
                "Choose circle(c), triangle(t), square(s) or a rectangle(r) to calculate its area: ")
            length_input = input(
                "Input the length\nFor a circle, this is the radius: ")
            width_input = input(
                "Input the width\nFor a triangle, this is the height, null for a circle: ")

            area = Area(length_input, width_input)
            result = area.calculate_area(user_input)
            print(f"The area is: {result}")

    # This "elif" is for if the user selects to calculate perimeter
        elif choose_calculation == "p":
            user_input = input(
                "Choose circle(c), triangle(t), square(s) or a rectangle(r) to calculate its perimeter: ")
            length_input = input(
                "Input the length\nFor a circle, this is the radius: ")
            width_input = input(
                "Input the width\nFor a triangle, this is the height, null for a circle: ")

            perimeter = Perimeter(length_input, width_input)
            result = perimeter.calculate_perimeter(user_input)
            print(f"The perimeter is: {result}")

        # This "elif" is if the user selects to calculate volume
        elif choose_calculation == "v":
            area_input = input("Enter the area to be calculated: ")
            height_input = input("Enter the height to be calculated: ")
            volume = Volume(area_input, height_input)
            result = volume.calculate_volume(area_input, height_input)
            print(f"The volume is: {result}")

        # This "elif" is if the user selects to exit the program entirely
        elif choose_calculation == "x":
            break


if __name__ == "__main__":
    main_program()
