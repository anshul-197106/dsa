# class Person:
#     def __init__(self, name):
#         self.name = name

#     def show(self):
#         print("Person Name:", self.name)

# class Student(Person):
#     def __init__(self, name, roll):
#         super().__init__(name)
#         self.roll = roll

#     def show(self):
#         print("Student Roll:", self.roll)
#         super().show   

# s = Student("Anshul", 101)
# s.show()

# Type Error 
# x = "hello"
# y = 15
# print(x + y)

# try:
#   x = "hello" 
#   y = 15

# except TypeError:
#   print("Please convert to string before concatenate")
# except:
#   print("Something else went wrong")

# try:
#     print(10 + 20)
# except TypeError:
#     print("tt");
# except ValueError:
#     print("vv");
# finally:
#     print("Completed")


# class Student(Exception):
# 1
    # try:
    #     a = 10
    #     b = "Hello"
    #     c = a + b
    #     print(c);
    # except TypeError as e:
    #     print("Type error:",e)
# s1 = Student()

# 2
#     def __init__(self, age):
#         if age < 18:
#             raise Exception("Age must be 18")
#         self.age = age;

# try:
#     s1 = Student(10)
#     print(s1.age)
# except Exception as e:
#     print (e)   

# Iterator -> object having iter() and next() methods
#iter() -> provide one value st as time and remember the state 
# list = [10, 20, 30]
# it = iter(list)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))


#Cycle iterator
# from itertools import cycle
# colors = cycle(["red", "green", "blue"]);
# # it = colors

# # print(next(it))
# for i in colors:
#     print(i)

# Generaor : A generator is a function that uses the yield keyword to return values one at a time and remembers its state between calls.
#
# def test():
#     yield 10
#     yield 20
#     yield 30

# it = test()
# print(next(it)) 
# print(next(it)) 
# print(next(it)) 

#  genrator ex
# def gen():
#         x = yield "Hello"
#         yield x;

# res = gen()
# print(next(res))
# #! send 
# print(res.send(10))


# create a fun that return even number form 1 to 10 
# def even_number():
#     for i in range(1, 11):
#         if i % 2 == 0:
#             yield i

# for num in even_number():
#     print(num)


#Access value from another generator --> Generator delegation
# def gen1():
#     yield 1
#     yield 2
# def gen2():
#     yield from gen1()
#     yield 3;
# it = gen2();
# print(next(it))
# print(next(it))
# print(next(it))


# generator expression

# gen = (x*x for x in range(6));
# it = gen;
# print(next(it))
# print(next(it))
# print(next(it))

# Meemory efficiency 

# def read():
#     with open("new.txt") as f:
#         for line in f:
#             yield line

# res = read()
# print(next(res))

# create 3 genrator 1 for even no(1-10), 1 for sum of odd number(1=10), 1 for sum of even sum of odd number(gen 1  and gen 2)
# def even_gen():
#     for i in range(1, 11):
#         if i % 2 == 0:
#             yield i

# def odd_sum_gen():
#     total = 0
#     for i in range(1, 11):
#         if i % 2 != 0:
#             total += i
#     yield total

# def total_sum_gen():
#     even_sum = sum(even_gen())
#     odd_sum = next(odd_sum_gen())
#     yield even_sum + odd_sum

# print("Even numbers are:")
# print(list(even_gen()))

# print("Sum of odd numbers:")
# print(next(odd_sum_gen()))

# print("Total sum (even + odd):")
# print(next(total_sum_gen()))

# closure --- inner func can remember the value of outer function
# decorators like a (==) closure
# 3 - layer function -- use parameter with decorator
# factory -- decorator -- wrapper

# def auth(role):
#     def dec(fx):
#         def wrapper():
#                 print("Greetings {role}")
#                 fx()
#         return wrapper
#     return dec

# @auth("admin")
# def hello():
#     print("Hello")

# hello()
 
# stack decorators 
# def dec1(fx):
#     def wrapper():
#         print("Before dec 1")
#         fx():
#         print("after dec 1")

#     return wrapper

# def dec2(fx):
#     def wrapper():
#         print("Before dec 2")
#         fx():
#         print("after dec 2")

#     return wrapper

# @dec1
# @dec2
# def test

# factory decorator 

# def fact(times):
#     def dec(fx):
#         def wrapper():
#             for _ in range(times):
#                 fx()
#         return wrapper
#     return dec

# @fact(3)
# def hey():
#     print("heyo")
# hey()


# def gen1():
#     try:
#         yield 1 
#     except ValueError:
#         print("ValueError")

# res = gen1()
# print(next(res))
# res.throw(ValueError)
