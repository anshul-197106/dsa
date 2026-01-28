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
class A:
    def show(self):
        print("A")
class B(A):
    def show(self):
        super().show()
        print("B")
class C(A):
    def show(self):
        super().show()
        print("C")

class D(B, C):
    def show(self):
        super().show()
        print("D")

obj = D()
obj.show()

