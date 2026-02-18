# Day 11-12: Functions, Arguments, Return Values

# function create greet message using arguments and return values. return values is send to the caller function

def greet(name):
    return f"Hello, {name}!"

print(greet("Kamal"))

def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)



# function create reusable code blocks to use callback
def reusable():
    return "This is reusable function"

print(reusable())

# function create welcome message using Arguments
def welcomeMsg(name):
    print(f"Welcome, {name}!")

welcomeMsg("Kamal Hassan")

# function create uppercase

def uppercase(name):
    return name.upper()

print(uppercase("kamal hassan"))

# function create lowercase

def lowercase(name):
    return name.lower()

print(lowercase("KAMAL HASSAN"))

# function create title case

def titlecase(name):
    return name.title()

print(titlecase("kamal hassan"))

# function create swap case

def swapcase(name):
    return name.swapcase()

print(swapcase("kamal hassan"))

# function create add two numbers using arguments
def add(a, b):
    return a + b

result = add(10, 20)
print("Sum:", result)


# file to access functions

from add_utils import add # here only imported add
print("Add:", add(10, 20))
# print("Sub:", sub(10, 20)) # show error not imported

import add_utils #use this if you want to use add_utils.add()
print("Add:", add_utils.add(10, 20))
print("Sub:", add_utils.sub(10, 20))
print("Mul:", add_utils.mul(10, 20))
print("Div:", add_utils.div(10, 20))
print("Mod:", add_utils.mod(10, 20))
print("Pow:", add_utils.pow(10, 20))
print("Sqrt:", add_utils.sqrt(10))
print("Cbrt:", add_utils.cbrt(10))

# Arguments (*args)
# *args is used to pass multiple arguments to a function
# *args is a tuple
# *args is a variable length argument

def addArgs(*args):
    total = 0 # 0 + 1 + 3 + 5 + 7 + 9 = 25
    for num in args: # 1, 3, 5, 7, 9
        total += num # 0 +=1, 1 +=3, 4 +=5, 9 +=7, 16 +=9
    return total # 25

print(addArgs(1,3,5,7,9)) # 25

# Keyword Arguments (*kwargs)
# *kwargs is used to pass multiple keyword arguments to a function
# *kwargs is a dictionary
# *kwargs is a variable length argument
# *kwargs is a keyword variable length argument
def create_profile(**kwargs):
    profile = ""
    for key, value in kwargs.items():
        profile += f"{key}: {value}\n"
    return profile

print(create_profile(name="Kamal Hassan", age=30, job="Software Engineer", city="Chennai", country="India", gender="Male"))