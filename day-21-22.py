# Day 21-22: Classes, Objects, OOP Basics

# class is blueprint
# object is instance of class
# __init__ is constructor
# self is reference to the current object

# Object creation (s1 is object)
class Person:
    def say_hello(self, name): # self is instance first parameter
        print("Hello, my name is", name)

s1 = Person()
s1.say_hello("Kamal")


# __init__ is constructor (it is used to initialize the object)
# self is reference to the current object
class Student:
    def __init__(self, name, age, grade): # constructor
        self.name = name
        self.age = age
        self.grade = grade

    def display(self): # method
        print(f"Hello, my name is {self.name} and I am {self.age} years old and I am in {self.grade} grade.")

p = Student("Kamal", 30, "C")
p.display()

# aathar example using constructor
class Employee:
    def __init__(self, name, aathar):
        self.name = name
        self.aathar = aathar

    def enter_office(self):
       print(f"{self.name} enters using aathar {self.aathar}")

    def open_bank_account(self):
        print(f"{self.name} opens bank account using aathar {self.aathar}")

    def apply_for_passport(self):
        print(f"{self.name} applies for passport using aathar {self.aathar}")

emp1 = Employee("Kamal", "123456789012")
emp1.enter_office()
emp1.open_bank_account()
emp1.apply_for_passport()

# mathTools using select self object with out constructor
class MathTools:
    def sqare(self, num):
        return num * num

    def cube(self, num):
        return num * num * num

    def add(self, num1, num2):
        return num1 + num2

    def sub(self, num1, num2):
        return num1 - num2

    def mul(self, num1, num2):
        return num1 * num2

    def div(self, num1, num2):
        return num1 / num2

tools = MathTools()
print(tools.sqare(5)) # output 25
print(tools.cube(5)) # output 125
print(tools.add(5, 5)) # output 10
print(tools.sub(5, 5)) # output 0
print(tools.mul(5, 5)) # output 25
print(tools.div(5, 5)) # output 1.0

# inheritance (one class acquires the properties of another class using code reusability)
# single inheritance
# multiple inheritance
# multi-level inheritance
# hybrid inheritance
# hierarchical inheritance

# diffents between multiple and multi-level inheritance
# multiple inheritance -> one child class inherits from multiple parent classes
# multi-level inheritance -> one child class inherits from one parent class, which inherits from another parent class

# single inheritance
class Parent: # parent
    def parent_method(self):
        print("Parent method")

a = Parent()
a.parent_method()

class Child(Parent): # child
    def child_method(self):
        print("Child method")

c = Child()
c.parent_method()
c.child_method()

# multiple inheritance
class Dad:
    def house(self):
        print("Dad has 2bhk house in chennai") #dad build
class Son:
    def car(self):
        print("Son has car in bangalore") # son car
class Child(Dad, Son):  # team one and two used only this class i am update this class new logic using vesion 3.0 overrided
    def child_method(self): # child
        print("Child method to update my new logic here")
    def house(self):
        print("Child has upgraded 3bhk house in chennai") # son updated house

c = Child()
c.house()
c.car()
c.child_method()
c.house()

# multi-level inheritance
class GrandParent:
    def grand_parent_method(self):
        print("Grand Parent method")

class Parent(GrandParent):
    def parent_method(self):
        print("Parent method")

class Child(Parent):
    def child_method(self):
        print("Child method")

c = Child()
c.grand_parent_method()
c.parent_method()
c.child_method()

# hybrid inheritance
class GrandParent:
    def grand_parent_method(self):
        print("Grand Parent method")

class Parent(GrandParent):
    def parent_method(self):
        print("Parent method")

class Child(Parent):
    def child_method(self):
        print("Child method")

class GrandChild(Child):
    def grand_child_method(self):
        print("Grand Child method")

gc = GrandChild()
gc.grand_parent_method()
gc.parent_method()
gc.child_method()
gc.grand_child_method()

# hierarchical inheritance
class GrandParent:
    def grand_parent_method(self):
        print("Grand Parent method")

class Parent(GrandParent):
    def parent_method(self):
        print("Parent method")

class Child(GrandParent):
    def child_method(self):
        print("Child method")

class GrandChild(Parent, Child):
    def grand_child_method(self):
        print("Grand Child method")

gc = GrandChild()
gc.grand_parent_method()
gc.parent_method()
gc.child_method()
gc.grand_child_method()

# create mobile app versions update using oop concepts
class App:
    def __init__(self, name, version):
        self.name = name
        self.version = version

    def update(self, new_version):
        self.version = new_version
        print(f"{self.name} updated to version {self.version}")

app = App("App", "1.0")
app.update("2.0")

# create mobile app versions update for bugs fixed updated new features using oop concepts
class App:
    def __init__(self, name, version):
        self.name = name
        self.version = version

    def update(self, new_version):
        self.version = new_version
        print(f"{self.name} updated to version {self.version}")

app = App("App", "1.0")
app.update("3.0")


