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