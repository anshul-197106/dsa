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

# Generaor : 
#
# def test():
#     yield 10
#     yield 20
#     yield 30

# it = test()
# print(next(it)) 
# print(next(it)) 
# print(next(it)) 


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

gen = (x*x for x in range(6));
it = gen;
print(next(it))
print(next(it))
print(next(it))

