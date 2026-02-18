# access modifiers
# public, private, protected (use methods or veriables)

class Parent:
    def public_method(self):
        print("public method")

    def _protected_method(self):
        print("protected method")

    def __private_method(self):
        print("private method")

    def access_from_same_class(self):
        print("accessing from same class")
        self.public_method()
        self._protected_method()
        self.__private_method()

class Child(Parent):
    def access_from_subclass(self):
        print("Inside child class (subclass)")
        self.public_method()
        self._protected_method()
        try:
            self.__private_method()
        except AttributeError as e:
            print(f"Private: ❌ cannot access (AttributeError: {e})")

class Stranger:
    def access_from_other_class(self, obj):
        print("Inside stranger class (other class)")
        obj.public_method()
        obj._protected_method() # ⚠️ Not recommended
        try:
            obj.__private_method() # ⚠️ Not recommended
        except AttributeError as e:
            print(f"Private: ❌ cannot access (AttributeError: {e})")

parent = Parent()
child = Child()
stranger = Stranger()

print("\n ➡️ access form SAME Class")
parent.access_from_same_class()

print("\n ➡️ access form SUB Class")
child.access_from_subclass()

print("\n ➡️ access form OTHER Class")
stranger.access_from_other_class(parent)

