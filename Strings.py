# Strings -> sequence of character
# immutable -> cannot be changed

# str = " a "
# str = ' b '
# str = ''' c '''


# str = "Python"
# print(str)

# functions(built in functions) and method(a function inside a class is called method)
# len, lower, upper, title, strip, replace, split, join, find, index, count
# str = "  Hello, Python Programming Language  "
# print(len(str))  # length of string
# print(str.lower())  # convert to lowercase
# print(str.upper())  # convert to uppercase  
# print(str.title())  # convert to title case
# print(str.strip())  # remove leading and trailing whitespace
# print(str.replace("Python", "Java"))  # replace substring
# print(str.split(","))  # split string into a list
# print("-".join(["Hello", "World"]))  # join list into a string with separator
# print(str.find("Python"))  # find substring index
# print(str.index("Programming"))  # find substring index (raises error if not found)
# print(str.count("a"))  # count occurrences of substring


# decorators -> function that modifies the behavior of another function
# def greet(fx):
#     def mfx():
#         print("Hi Class")
#         fx()
#         print("Function execution completed.")
#     return mfx;

# @greet
# def show():
#     print("Hello, World!")
# show();

# greet(show)();


# def decorator_function(original_function):
# def greet(fx):
#     def mfx():
#         print("rororo")
#         fx()
#         print("🔥🔥")
#     return mfx;

# @greet
# def show():
#     print("asdfghjkl");
# show();

# greet(show)();


# from function import show
# def greet(fx):
#     def mfx(a,b):
#         print("rororo")
#         fx(a,b)
#         print(" aws ")
#     return mfx;

# @greet
# def add(a,b):
#     print(a + b);
# show();

# greet(add)(10,20);

#regex -> regular expression -> pattern matching
# search the word from strings
import re
text = "Hello World";
result = re.search("World", text)
if result:
    print("Match found")

# generate list of word with the findball
# s = "cat bat rat mat"
# print(re.findall("at", s))

# split 
# import re
# str = "Python is a high level"
# result = str.split(" ",);
# print(result)


# from math import *
# print(sqrt(58));

# import calc
# calc.add(10,20)

# from datetime import datetime
# a  = datetime.now()
# print(a)

# print specific time and date with the help of time date module 


# random module
# import random
# print(random.random())

# random.seed(4);
# print(random.randint(1, 8));
