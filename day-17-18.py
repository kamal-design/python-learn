# Day 17-18: File Handling (read/write), Exceptions

# Modes (one-liner summary):
""" Modes are used to open the file in different modes
    Mode    Description
    'r'     Read-Only (file must exist)
    'w'     Write-Only (file will be created if not exist, else overwritten)
    'a'     Append-Only (file will be created if not exist, else appended)

    'x'     Exclusive-Creation (file will be created if not exist, else error)
    'b'     Binary mode
    't'     Text mode
    '+'     Read and Write

    'r+'    Read and Write (file must exist)
    'w+'    Write and Read (file will be created if not exist, else overwritten)
    'a+'    Append and Read (file will be created if not exist, else appended)

    'rb'    Read Binary
    'wb'    Write Binary
    'ab'    Append Binary
"""


# File handling
# file = open("notes.txt", "node")

# w Write-Only (file will be created if not exist, else overwritten)
file = open("notes.txt", 'w')
file.write("Welcome to Python file handling!\n")
file.write("This is a new file.\n")
file.close()

# r Read-Only
file = open("notes.txt", 'r')
content = file.read()
print("File content:\n", content) # file text printed
file.close()

# a Append-Only (file will be created if not exist, else appended)
# file = open("notes.txt", 'w') #this overwritten
file = open("notes.txt", 'a')
file.write("This is an appended text.\n adding a new line\n")
file.close()

# with is automaic file close

with open("notes.txt", "r") as file: #f is file
    for line in file:
        print(line.strip()) # output file text show
        print("\n")

with open("sample.txt", 'w') as f:
    f.write("Hello, file! new added text day 17-18")
    print("\n")

with open("sample.txt", "r") as f:
    content = f.read()
    print(content)
    print("\n")

# feedback = input('Enter your feedback:')
# with open('feedback-log.txt', 'a') as log:
#     log.write(feedback + "\n")

print('Thanks for your feedback is saved.')


with open("feedback-log.txt", 'r') as file:
    # print(file.readline().strip()) # sing line to read
    # print(file.readline().strip())
    # print(file.readline().strip())
    while True:
        line = file.readline()
        if not line:
            break
        if "ERROR" in line: # show file ERROR line
            print("Found error: ⚠️", line.strip())
            print("\n")

with open ('feedback-log.txt') as f: # file
    for _ in range(4): # read first 4 lines with _ throw away variable
        print(f.readline().strip())
        print("\n")

#  CSV file handling
with open("input_file.csv", "r") as infile, open("output_file.csv", "w") as outfile:
    for line in infile:
        print(line.strip())
        outfile.write(line)
    print("\n")

# method one
import csv
with open("input_file.csv", "r") as file:
    reader = csv.DictReader(file)
    print("feach each row age only")
    for row in reader:
        print(row["age"])
    print("\n")

# method Two
with open("input_file.csv", "r") as file:
    reader = csv.reader(file)
    print("feach each row age only")
    for row in reader:
        print(row[2])
    print("\n")

# csv file handling with Column names
with open("input_file.csv", "r") as file:
    lines = file.readlines();
    print("feach each row City only")
    for line in lines[1:]: # skip header line
        columns = line.strip().split(',') # split by comma
        # columns[0] -> name, columns[1] -> city, columns[2] -> age
        print(columns[1]) # assuming age is the third column (index 2)
    print("\n")


# Exception handling ---> try throw except finally

# What is an exception? -> An exception is an error that occurs during the execution of a program. It disrupts the normal flow of the program and can cause it to terminate if not handled properly.

# what is exception handling? -> Exception handling is the process of responding to exceptions in a controlled manner. It allows developers to write code that can gracefully handle errors and continue execution without crashing the program.

# what is error handling? -> Error handling is the process of anticipating, detecting, and resolving errors in a program. It involves writing code to manage and respond to errors that may occur during the execution of a program.
# print hi -> syntax error
# a=10 -> indentation error
# a/0 -> zero division error
# int("abc") -> value error

# if else to handle error but it is not efficient and not recommended (not identify all error types or handle all error scenarios) best way to handle error is using exception handling with try-except blocks finally block to ensure that certain code is always executed regardless of whether an exception occurred or not.

# a = 10
# b = 0
# if b != 0:
#     result = a / b
#     print("Result:", result)
# else:
#     print("Cannot divide by zero!")


# ZeroDivisionError -> when you try to divide a number by zero
# ValueError -> when you try to convert a string that cannot be converted to a number
# TypeError -> when you try to perform an operation on a data type that is not supported
# IndexError -> when you try to access an index that is out of range
# KeyError -> when you try to access a key that does not exist in a dictionary
# AttributeError -> when you try to access an attribute that does not exist in an object
# FileNotFoundError -> when you try to open a file that does not exist
# SyntaxError -> when you have a syntax error in your code
# IndentationError -> when you have an indentation error in your code
# Exception -> the base class for all exceptions, you can catch any exception using this class
# RecursionError -> when you have a recursive function that exceeds the maximum recursion depth
# ImportError -> when you try to import a module that does not exist
# NameError -> when you try to use a variable that is not defined
# ModuleNotFoundError -> when you try to import a module that does not exist
# MemoryError -> when your program runs out of memory
# StopIterationError -> when you have an iterator that has no more items to return
# IOError -> when you have an input/output error, such as trying to read a file that does not exist or trying to write to a file that is read-only

# error to don't crach hole program or app -> continue to run next step

# try anothor way:
a = 10
b = 0
# result = a / b # crached here
# print("Result:", result) # this line will not execute due to the exception

# python default ZeroDivisionError
try:
    x = 1 / 0 # one and 0 division error
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Done") # finally block will always execute regardless of whether an exception occurred or not
print("\n")

# Exception handling with user input 0 to crach program

# print("Welcome to Zomato!")
# number_of_items = int(input("Enter the number of items you want to order?")) # input 0 to crach here
# total_cost  = 200 * number_of_items
# avarage_cost = total_cost / number_of_items # this line will raise ZeroDivisionError if number_of_items is 0
# print(f"Total cost: {total_cost}, Average cost per item: {avarage_cost}")

# Exception handling with user input 0 to no crach program
try:
    print("Welcome to Zomato!")
    number_of_items = int(input("Enter the number of items you want to order?")) # input 0 to crach here
    total_cost  = 200 * number_of_items
    avarage_cost = total_cost / number_of_items # this line will raise ZeroDivisionError if number_of_items is 0
    print(f"Total cost: {total_cost}, Average cost per item: {avarage_cost}")
except ZeroDivisionError: # user condition to handle zero division error
    print("You cannot order zero items! Please enter a valid number of items.")

print("Thank you for using Zomato!")
print("\n")


# Exception handling with no idea about error type
try:
    print("No idea about error type")
    number_of_items = int(input("Enter the number of items you want to order?")) # input 0 to crach here
    total_cost  = 200 * number_of_items
    avarage_cost = total_cost / number_of_items # this line will raise ZeroDivisionError if number_of_items is 0
    print(f"Total cost: {total_cost}, Average cost per item: {avarage_cost}")
except Exception as e: # catch any exception and print the error message
    print("An error occurred:", str(e))

print("Thank you for using Exception")
print("\n")

# Exception handling with multiple except blocks ( 0, string, etc.. input)
try:
    print("Multiple except blocks")
    number_of_items = int(input("Enter the number of items you want to order?")) # input 0 to crach here
    total_cost  = 200 * number_of_items
    avarage_cost = total_cost / number_of_items # this line will raise ZeroDivisionError if number_of_items is 0
    print(f"Total cost: {total_cost}, Average cost per item: {avarage_cost}")
except ZeroDivisionError:
    print("You cannot order zero items! Please enter a valid number of items.")
except ValueError:
    print("Invalid input! Please enter a valid number of items.")
except Exception as e:
    print("An error occurred:", str(e))
print("Thank you for using Multiple except blocks")
print("\n")

# Exception handling with finally block using bank account example
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        try:
            print("Processing withdrawal...")
            if amount > self.balance:
                raise ValueError("Insufficient funds!")
            self.balance -= amount
            print(f"Withdrawal successful! Remaining balance: {self.balance}")
        except ValueError as e:
            print("Error:", str(e))
        finally:
            print("Thank you for banking with us!")
print("ATM withdrawal example with exception handling")

account = BankAccount(1000)
account.withdraw(500)  # this will be successful withdrawal
account.withdraw(2000) # this will raise ValueError for insufficient funds
print("\n")

# Exception handling with nested try-except blocks
try:
    print("Zomoto Login successful!")
    number_of_items = int(input("Enter the number of items you want to order?")) # input 0 to crach here
    total_cost  = 200 * number_of_items
    avarage_cost = total_cost / number_of_items # this line will raise ZeroDivisionError if number_of_items is 0
    print(f"Total cost: {total_cost}, Average cost per item: {avarage_cost}")
except ZeroDivisionError:
    print("You cannot order zero items! Please enter a valid number of items.")
except ValueError:
    print("Invalid input! Please enter a valid number of items.")
except Exception as e:
    print("An error occurred:", str(e))
finally:
    print("Logout successful! Thank you for using Zomato!") # finally block will always execute regardless of whether an exception occurred or not

print("Execution run always no block will be skipped due to exception handling\n")