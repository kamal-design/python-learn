# Day 21-22: Classes, Objects, OOP Basics

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

p = Person("Kamal", 30)
p.greet()
