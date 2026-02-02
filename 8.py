class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Person Name:", self.name)

class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll

    def show(self):
        print("Student Roll:", self.roll)
        super().show   

s = Student("Anshul", 101)
s.show()

Type Error 
x = "hello"
y = 15
print(x + y)

try:
  x = "hello" 
except TypeError:
  print("Please convert to string before concatenate")
except:
  print("Something else went wrong")
