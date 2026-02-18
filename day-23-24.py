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

# Polymorphism (many forms using overriding)
class Dog:
    def speak(self):
        print("Dog barks")

class Cat:
    def speak(self):
        print("Cat meows")

def animal_speak(animal):
    animal.speak()

animal_speak(Dog())
animal_speak(Cat())

# Abstraction (hiding the implementation details)
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius

circle = Circle(5)
print(circle.area())

# abstract class used for user input methods
class FeatruePlan(ABC):
    @abstractmethod # abstract class don't create objects
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass

    def checkout(self): #checkout not abstract method
        pass

class WebApp(FeatruePlan):
    def login(self):
        return "Web App Login Done 👍"
    def logout(self):
        return "Web App Logout Done 👍"
    def checkoutChange(self): # here new one added not checkout used
        return "Web App Checkout Done chnaged 👍"

class MobileApp(FeatruePlan):
    def login(self):
        return "Mobile App Login Done 👍"
    def logout(self):
        return "Mobile App Logout Done 👍"
    def checkout(self):
        return "Mobile App Checkout Done 👍"

webApp = WebApp()
mobileApp = MobileApp()

print(webApp.login())
print(webApp.logout())
print(webApp.checkout()) #here parent only access not overriding
print(webApp.checkoutChange()) #here parent and child access overriding
print(mobileApp.login())
print(mobileApp.logout())
print(mobileApp.checkout()) #here parent and child access overriding
