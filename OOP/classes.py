# Python Object-Oriented Programming by C Schafer

# Lesson 1: Classes and Instances

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@company.co"
        self.pay = pay

    def fullname(self):
        return f"{self.first} {self.last}"

emp_1 = Employee("Dee", "Palmer", 100000)
emp_2 = Employee("Lee", "King", 60000)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
print(emp_2.fullname())