# attributes are what an object knows and methods arw what an object can do


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


s1 = Student("Mary", 24)
s2 = Student("Ted", 21)


class Car:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print(self.brand, "is driving")


c1 = Car("Toyota")
c1.drive()

c2 = Car("Nissan")
c2.drive()
