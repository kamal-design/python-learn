# Day 23-24: Inheritance, Polymorphism, Encapsulation

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

d = Dog()
d.speak()

# Encapsulation
class Car:
    def __init__(self):
        self.__speed = 0
    def set_speed(self, speed):
        self.__speed = speed
    def get_speed(self):
        return self.__speed
car = Car()
car.set_speed(60)
print(car.get_speed())
