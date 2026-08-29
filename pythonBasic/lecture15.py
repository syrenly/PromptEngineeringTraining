# inheritance=same method as base/parent class plus new method


class Vehicle:  # parent class
    def move(self):
        print("The vehicle is moving")


class Car(Vehicle):  # child class
    def honk(self):
        print("The car is honking")


c1 = Car()
c1.move()
c1.honk()

# polymorphism=same name method, but different behavior


class Animal:
    def speak(self):
        print("Animal speaks")


class Dog(Animal):
    def speak(self):
        print("Dog speaks")


class Cat(Animal):
    def speak(self):
        print("Cat speaks")


animals = [Cat(), Dog()]
for a in animals:
    a.speak()
