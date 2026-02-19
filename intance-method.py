# Instance method (object)
# Class method
# Static method

# class leval method
class Employee:
    company = 'Open AI' # class leval data

    @classmethod
    def change_company(cls, new_name):
        cls.company = new_name # accessing class variable

print(f"Company name is {Employee.company}") # Output: Open AI

Employee.change_company('Google') # class lavel to change
print(f"Company name is {Employee.company}") # Output: Google


# static leval method (this one not defendent on class and object. utility method)
class Math:
    @staticmethod
    def add(a, b):
        return a + b

print(f"static method: {Math.add(10, 12)}") # 👉 22


# call both methods (class & static)
class ProfileCheck:
    company_name = 'Open AI' # class leval data

    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name # access class variable

    @staticmethod
    def try_change_company(new_name):
        company_name = new_name # local variable inside only

ProfileCheck.change_company('Google')
print("\n After classmethod:", ProfileCheck.company_name)

ProfileCheck.try_change_company('Microsoft')
print("\n After staticmethod:", ProfileCheck.company_name)
print("\n")

# Example
class myClass:
    def instance_method(self):
        print("Called Instance method")

    @classmethod
    def class_method(cls):
        print("Called Class method")

    @staticmethod
    def static_method():
        print("Called Static method")

obj = myClass()
obj.instance_method()
myClass.class_method()
myClass.static_method()