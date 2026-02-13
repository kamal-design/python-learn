# Day 3-4: Input/Output, Basic Operators, String Manipulation

# Input/Output Example
name = input("Enter your name: ")
print("Hello,", name)

# Basic Operators Example #Arithmetic Operators
a = 10
b = 3
print("Addition:", a + b) # 10 + 3 = 13
print("Subtraction:", a - b) # 10 - 3 = 7
print("Multiplication:", a * b) # 10 * 3 = 30
print("Division:", a / b) # 10 / 3 = 3.3333333333333335 (float division)
print("Floor Division:", a // b) # 10 // 3 = 3 (integer division)
print("Modulus:", a % b) # 10 % 3 = 1 (remainder)
print("Exponent:", a ** b) #10 * 10 * 10 = 1000

# Comparison Operators
x = 5
y = 10
print("Equal:", x == y)          # False
print("Not Equal:", x != y)      # True
print("Greater Than:", x > y)    # False
print("Less Than:", x < y)       # True
print("Greater or Equal:", x >= y) # False
print("Less or Equal:", x <= y)    # True

# Logical Operators
p = True
q = False
print("AND:", p and q)  # False
print("OR:", p or q)    # True
print("NOT p:", not p)  # False
print("NOT q:", not q)  # True

# bitwise operators
a = 5  # 0101 in binary
b = 3  # 0011 in binary
print("Bitwise AND:", a & b)  # 1 (0001 in binary)
print("Bitwise OR:", a | b)   # 7 (0111 in binary
print("Bitwise XOR:", a ^ b)  # 6 (0110 in binary)
print("Bitwise NOT a:", ~a)    # -6 (in two's complement)
print("Bitwise NOT b:", ~b)    # -4 (in two's complement)
print("Left Shift a by 1:", a << 1)  # 10 (1010 in binary)
print("Right Shift a by 1:", a >> 1) # 2 (0010 in binary)


# String Manipulation Example
s = "Hello, Python World!"
print("Original:", s)
print("Lowercase:", s.lower()) #hello, python world!
print("Uppercase:", s.upper()) #HELLO, PYTHON WORLD!

print(s.replace("World", "Python"))  # Hello, Python!
print(s.split(","))      # ['Hello', ' World!']
print(s.strip("!"))      # Hello, World

# Slicing [start:stop:step]
print("Slice [0:5]:", s[0:5])           # Hello
print("Every 2nd char:", s[::2])        # Hlo yhnWrd
print("Reverse string:", s[::-1])       # !dlroW nohtyP ,olleH

# String Formatting (Modern f-strings)
version = 3.12
print(f"I am learning Python {version} and I love it!")

# Membership
print("Python" in s) # True
print("Java" not in s) # True

# Realtime coding example
amount = 1200
tax = amount * 0.18
total_amount = amount + tax
print("Amount:", amount)
print("Tax:", tax)
print("Tax percentage:", tax / amount * 100, "%")

if total_amount > 1000:
    print("Total amount with tax is:", total_amount)
    discount = total_amount * 0.10
    total_amount -= discount
    print("Total amount after discount is:", total_amount)
else:
    print("Total amount with tax is:", total_amount)

# Movie ticket price calculation using logical operators
age = 20
student = 'yes'

if age < 12 or student == 'yes':
    print("You are eligible for a discounted ticket price.")
else:
    print("You need to pay the full ticket price.")


if age >= 60 and student == 'yes':
    print("You are eligible for a senior citizen discount.")
else:
    print("You are not eligible for a senior citizen discount.")