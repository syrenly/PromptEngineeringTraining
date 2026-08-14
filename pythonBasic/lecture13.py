# class = definition, object = instance

class Student:
    name="John"
    age=20
    def greet(self): # function inside a class is a method; `self` means that this refer to the current object
        print("Hello, I am a student")

s1=Student()

print("Age:", s1.age)
print("Name", s1.name)
s1.greet()

# initialization of a class; implement `__init__` method

class Student2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s2= Student2("Alice", 25)
s3= Student2("Tudor", 30)

print("Student 2", s2.name)
print("Student 3", s3.name)