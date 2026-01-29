# assignment 2
# Email Validation program

# import re

# emails = input("Enter emails: ").split()
# pattern = r"^\w+@gmail\.com$"

# for email in emails:
#     print(email, "Valid" if re.match(pattern, email) else "Invalid")


# Password Strength Checker
# a = input("Password: ")

# u = l = d = s = 0
# for ch in a:
#     if ch.isupper():
#         u = 1
#     elif ch.islower():
#         l = 1
#     elif ch.isdigit():
#         d = 1
#     else:
#         s = 1

# if len(a) >= 8 and u and l and d and s:
#     print("Strong Password")
# else:
#     print("Weak Password")


# OTP Generator
# import random
# import string

# otp6 = random.randint(100000, 999999)
# print("6-digit OTP:", otp6)

# chars = string.ascii_letters + string.digits
# otp8 = ""

# for i in range(8):
#     otp8 = otp8 + random.choice(chars)

# print("8-character OTP:", otp8)
  

# Dice Game Solution
# import random

# dice = random.randint(1, 6)
# print("Dice:", dice)

# if dice == 6:
#     print("You win")
# else:
#     print("Try again")


# Abstract Class Example
# from abc import ABC, abstractmethod
# import math

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Rectangle(Shape):
#     def __init__(self, l, b):
#         self.l = l
#         self.b = b

#     def area(self):
#         return self.l * self.b

# class Circle(Shape):
#     def __init__(self, r):
#         self.r = r

#     def area(self):
#         return math.pi * self.r * self.r

# r = Rectangle(5, 4)
# c = Circle(3)

# print("Rectangle Area:", r.area())
# print("Circle Area:", c.area())

