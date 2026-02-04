# Day 3-4: Input/Output, Basic Operators, String Manipulation

# Input/Output Example
name = input("Enter your name: ")
print("Hello,", name)

# Basic Operators Example
a = 10
b = 3
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

# String Manipulation Example
s = "Hello, World!"
print(s.lower())         # hello, world!
print(s.upper())         # HELLO, WORLD!
print(s[0:5])            # Hello
print(s.replace("World", "Python"))  # Hello, Python!
print(s.split(","))      # ['Hello', ' World!']
print(s.strip("!"))      # Hello, World
