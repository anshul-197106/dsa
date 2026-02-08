# create a library management system use OOPS
from abc import ABC, abstractmethod
class Item(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def info(self):
        pass

class Book(Item):
    def __init__(self, name, author, available=True):
        super().__init__(name)
        self.author = author
        self.available = available

    def info(self):
        status = "Available" if self.available else "Not Available"
        return self.name + " - " + self.author + " (" + status + ")"

    def borrow(self):
        if self.available:
            self.available = False
            return True
        return False

    def return_book(self):
        self.available = True

class Library:
    def __init__(self):
        self.__books = []

    def add_books(self, book):
        self.__books.append(book)

    def show_books(self):
        for b in self.__books:
            print(b.info())

# class student  (info,issue, return )

lib = Library() 

b1 = Book("Python", "adbh")
b2 = Book("Java", "ffji")

b2.borrow()

lib.add_books(b1)
lib.add_books(b2)

lib.show_books()
