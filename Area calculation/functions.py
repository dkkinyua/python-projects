"""
A custom module to calculate various areas of various shapes and display their area

"""


def circle_area(n1):
    area = (3.14 * n1 ** 2) / 4
    return area


def triangle_area(n1, n2):
    area = 0.5 * n1 * n2
    return area


def rectangle_area(n1, n2):
    area = n1 * n2
    return area


def trapezium_area(a, b, c):
    area = 0.5 * c * (a + b)
    return area
