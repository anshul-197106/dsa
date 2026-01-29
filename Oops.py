# OOPS --> Re-usability -> DRY
# Code Structure
# Real world implementation


# class Student:
#     # Attributes
#     id = ""
#     name = ""
#     salary = ""
    
#     # Method
#     def show(self):
#         print("Id is :",self.id)
#         print("name is :",self.name)
#         print("salary is :",self.salary)

# s1 = Student() #object create 
# s1.id = 1
# s1.name = "As"
# s1.salary = "50000"
# s1.show()

# s2 = Student()
# s2.id = 2
# s2.name = "Aw"
# s2.salary = "80000"
# s2.show()

# class Employee:
#     company = "Google"; #class variable
#     def setDetails(self, id, name):
#         self.name = name;
#         self.id = id;

# def showDetails(self):
#     print(f"Name is : {self.name} and id is {self.id} --> {self.company}")


# class Bank: 
#     def showDetails(self, name, deposit, withdraw):
#         self.name = name;
#         self.deposit = deposit
#         self.withdraw = withdraw

# b = Bank()
# b.showDetails("Ansh","2500","5620")
# print (b.name)



# class Student:
#     college = "ASD"   # class variable

#     def details(self, name, id):
#         self.name = name
#         self.id = id

#     def show(self):
#         print("College:", Student.college)
#         print("Name:", self.name)
#         print("ID:", self.id)


# s1 = Student()          # create object
# s1.details("ashj", 27)  # set data
# s1.show()



# class Student:
#     college = "LPU" #class variable

#     def __init__(self,name):
#         self.name = name;

# s1 = Student("labesh");
# print(s1.name)


# class Bank:
#     def __init__(self, name, balance=0):
#         self.name = name
#         self.balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"{amount} deposited. New balance: {self.balance}")
#         else:
#             print("Deposit amount must be positive.")

#     def withdraw(self, amount):
#         if 0 < amount <= self.balance:
#             self.balance -= amount
#             print(f"{amount} withdrawn. New balance: {self.balance}")
#         else:
#             print("Insufficient balance or invalid amount.")

#     def get_balance(self):
#         return self.balance


# account = Bank("Alice", 1000)
# account.deposit(500)
# account.withdraw(300)
# print("Final Balance:", account.get_balance())

# Inheritence ->  allows us to define a class that inherits all the methods and properties from another class.
# parent 

# class A: #parent class
#     def showA(self):
#         print("A")

# class B(A): #child class
#     def showB(self):
#         print("B")

# obj = B()
# obj.showB();
# obj.showA()

# Constructor overloading
# class Vehicle:
#     def __init__ (self,model,color):
#         self.model = model
#         self.color = color

#     def show(self):
#         print("Model: ",self.model)
#         print("Color: " ,self.color)

# class Car(Vehicle): 
#     def __init__(self, model, color, seats):
#         super().__init__(model, color)
#         self.seats = seats

#     # ! Method overriding
#     def show(self):
#         super().show() # super -> calling parrent class into child class
#         print("Seats: ",self.seats)

# v1 = Vehicle("Audi","Black")
# v1.show()
# c1 = Car("Jaguar","White","2")
# c1.show()


# single level inheritence -> one parent one child
# Hierarical -> A -> B -> C
# class A:
#     def showA(self):
#         print("A")
# class B(A):
#     def showB(self):
#         print("B")
# class C(A):
#     def showC(self):
#         print("C") 
# class D(B, C):
#     def showD(self):
#         print("D")

# obj = D()
# obj.showA()
# obj.showB()
# obj.showC()
# obj.showD()

# Multiple inheritence : a child having multiple parents


# Diampnd Problem 

# Diampnd Problem 
# class A:
#     def show(self):
#         print("A")
# class B(A):
#     def show(self):
#         super().show()
#         print("B")
# class C(A):
#     def show(self):
#         super().show()
#         print("C")

# class D(B, C):
#     def show(self):
#         super().show()
#         print("D")

# obj = D()
# obj.show()
 
# class Animal:
#     def speak(self):
#         return "Some generic animal sound"

# class Dog(Animal):
#     # Overriding the speak method
#     def speak(self):
#         return "Woof! Woof!"

# # Create objects
# generic_animal = Animal()
# my_dog = Dog()

# # Call the method
# print(f"Generic animal sound: {generic_animal.speak()}")
# print(f"Dog sound: {my_dog.speak()}")


#   polymorphism - method can behave different 
#   super + overriding --> runtime polymorphism

#    Encapsualtion - binding the data
#    Access modifiers --> public, private, protected    

# class Employee:
#     def __init__(self):
#         self.name = "Empty";
#         self.__id = 123;

#     def getId(self):
#         return self.__id
    
#     def setId(self,value):
#         self.__id = value
    
# obj = Employee();
# obj.setId(2);
# print(obj.getId())
# print(obj._id) #single _ protected , #double __ protected


# class Students:
#     def __init__(self):
#         self.__name = "Asdf"
#         self.__age = 11
#         self.__marks = 87

#     def getId(self):
#         return self.__name, self.__age, self.__marks

#     def setId(self, name, age, marks):
#         self.__name = name
#         self.__age = age
#         self.__marks = marks

# obj = Students()
# obj.setId("John", 15, 92)
# print(obj.getId())


# class Student:
#     def __init__(self, marks):
#         self.__marks = marks

#     @property
#     def marks(self): #getter
#         return self.__marks
    
#     @marks.setter
#     def marks(self, value):
#         self.__marks = value

# s1 = Student(80)
# s1.marks = 90
# print(s1.marks)

#                         abstraction --> Hiding the implementations or showing essential details
#? security

# Abstract Class --> Always act like base class (it can have both abstract and non-abstract methods)

# from abc import ABC, abstractmethod
# class Employee(ABC) :#abstract class
#     @abstractmethod
#     def greet(self):#abstract method
#         pass;
#     def hello(self):
#         print("Hello.... :")

# class Technical(Employee):
#     def greet(self):
#         print("Hii...")

# obj = Technical();
# obj.greet()
# obj.hello()
 

# from abc import ABC, abstractmethod
# class ATM(ABC):
#     @abstractmethod
#     def withdraw(self, amount):
#         pass

# class SBI(ATM):
#     def withdraw(self, amount):
#         print("Accessing bank account...")
#         print("Amount withdrawn:", amount)

# atm = SBI()
# atm.withdraw(50000)


# class AgeNotValid(Exception):
#     pass

# class Person:
#     def __init__(self, age):
#         if age < 18:
#             raise AgeNotValid("Age should not be below 18")
#         self.age = age   # store the actual age

# try:
#     obj = Person(20)   # pass age here
#     print(obj.age)
# except AgeNotValid as e:
#     print(e)

class Student:
    def __init__(self, name, marks):
        if not (0 <= marks <= 100):
            raise ValueError("Marks must be between 0 and 100")
        self.name = name
        self.marks = marks

try:
    s1 = Student("Alice", 85)   
    print(f"{s1.name} scored {s1.marks}")
    
    s2 = Student("Bob", 120)   
    print(f"{s2.name} scored {s2.marks}")

except ValueError as e:
    print("Error:", e)