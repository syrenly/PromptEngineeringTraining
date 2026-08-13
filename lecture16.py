# encapsulation=control which attributes and methods can be accessible from the outside

class BankAccount:
    def __init__(self, balance):
        self._balance=balance # _ means protected; __ means private
    def get_balance(self):
        return self._balance
    def deposit(self,amount):
        self._balance += amount

# abstraction= show only what is needed and hide the implementation

class Printer:
    def print_document(self):
        print("printing document")

Printer().print_document()

class Shape:
    def area(self):
        pass # do not declare the implementation

class Circle(Shape):
    def area(self):
        print("calculating area")

Shape().area() # nothing happens
Circle().area()

