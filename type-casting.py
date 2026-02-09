# Type Casting in Python
# Type casting is the process of converting a variable from one data type to another. In Python, you can use built-in functions to perform type casting. Here are some examples:

x = '10'
print(type(x))  # Output: <class 'str'>
print(x + '20')  # Output: '1020' (string concatenation)
print(int(x) + 20)  # Output: 30 (integer addition)
print(float(x) + 20.5)  # Output: 30.5 (float addition)
print(str(10) + '20')  # Output: '1020' (string concatenation)

a = '11'
b= '4'

print(a + b)  # Output: '114' (string concatenation)
print(type(a))  # Output: <class 'str'>
print(int(a) + int(b))  # Output: 15 (integer addition)

c = '3.14'
# print(int(c))  # Output: ValueError: invalid literal for int() with base 10: '3.14' (cannot convert float string to int)
print(type(c))  # Output: '3.14' (float to string)
print(float(c) + 2)  # Output: 5.14 (float addition)
print(type(float(c) + 2))  # Output: <class 'float'> (result of float addition is a float)

y = 'A'
z = 'B'
print(y + z)  # Output: 'AB' (string concatenation)
print(ord(y))  # Output: 65 (ASCII value of 'A')
print(ord(z))  # Output: 66 (ASCII value of 'B')
print(chr(65))  # Output: 'A' (character for ASCII value 65)
print(chr(66))  # Output: 'B' (character for ASCII value 66)
