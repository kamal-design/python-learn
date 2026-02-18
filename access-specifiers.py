# access specifiers
# public, private, protected (use methods or veriables)

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display(self):
        print(self.make, self.model, self.year)

car = Car("Toyota", "Camry", 2022)
car.display()

# public -> access anywhere
# _protected -> access only in class
# __private -> access in class and child class

class Parent:
    def __init__(self):
        self.public_var = "I am public"
        self._protected_var = "I am protected"
        self.__private_var = "I am private"

    def access_from_same_class(self):
        print("Inside parent Class:")
        print("Public:", self.public_var)
        print("Protected:", self._protected_var)
        print("Private:", self.__private_var)

class Child(Parent):
    def assess_form_subclass(self):
        print("Inside child Class (SubClass)")
        print("public:", self.public_var)
        print("protected:", self._protected_var)
        print("private:", self._Parent__private_var)
        try:
            print("private:", self.__private_var) #don't access private in subclass
            # print("private:", self._Parent__private_var) #access private in subclass (by name mangling) desipline breaker
        except AttributeError as e:
            print(f"Privete: ❌ cannot access (AttributeError: {e})" )

class Stranger:
    def assess_form_other_class(self, obj):
        print("Inside Stranger Class (Unrelated)")
        print("public:", obj.public_var)
        print("protected:", obj._protected_var) # ⚠️ Not recommended
        try:
            print("private:", obj.__private_var)
        except AttributeError as e:
            print(f"Privete: ❌ cannot access (AttributeError: {e})" )

p = Parent()
c = Child()
s = Stranger()


print("\n ➡️ access form SAME Class")
p.access_from_same_class()

print("\n ➡️ access form SUB Class")
c.assess_form_subclass()

print("\n ➡️ access form OTHER Class")
s.assess_form_other_class(p)

