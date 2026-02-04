# Day 17-18: File Handling (read/write), Exceptions

# File handling
with open("sample.txt", "w") as f:
    f.write("Hello, file!")

with open("sample.txt", "r") as f:
    content = f.read()
    print(content)

# Exception handling
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Done")
