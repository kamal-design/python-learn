# python use input() function to take input from user
name = input("Enter your name: ")
print("Hello, " + name + "! Welcome to Python programming.")

# Change magenagement process
# 1. Identify the change
# 2. Assess the impact
# 3. Plan the change
# 4. Implement the change
# 5. Test the change
# 6. Review and document the change

'''
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
sum = a + b
print("The sum of", a, "and", b, "is:", sum)
'''

# shaduling directly not accessible in python but we can use libraries like schedule or time to achieve it. input not directly but we can use it to trigger the shaduling code.

# run this code in terminal with command: python3 inputs.py "Kamal hassan" "hassan" (first argument is the full name and second argument is the last name) and it will generate the email based on the full name and last name provided. we can use sys.argv to take multiple inputs from command line.

#cmd to run --->  python3 inputs.py Kamal hassan

# run this code in terminal with command: python3 file[0] name[1] (name is the variable which will take the input from command line) sys.argv[0] is the name of the file and sys.argv[1] is the first argument passed to the file (name in this case) and so on. we can use sys.argv to take multiple inputs from command line.


# method 1: using input() function to take input from user
# check sys.argv and take multiple inputs from command line and generate email based on the full name and last name provided. we can use sys.argv to take multiple inputs from command line.
"""
import sys
if len(sys.argv) == 2:
    print('Usage: python inputs.py <full_name> <last_name>')
    sys.exit()


full_name = sys.argv[1]
last_name = sys.argv[2] # full_name.split()[1] # split the full name and take the second part as last name

# formatting the string (name)
email = full_name.lower().replace(" ", ".")+ last_name + "@deign.com"

# output
print("\n--- User Information ---")
print("Full Name:", full_name)
print("Generated Email:", email)

"""


# method 2: using input() function to take input from user no limit on the number of inputs
# CMD to run ---> python3 inputs.py Kamal hassan m
# output will be ---> Full Name: Kamal hassan m
# Generated Email: kamal.hassan.m@deign.com

import sys
if len(sys.argv) == 2:
    print('Usage: python inputs.py <full_name> <last_name>')
    sys.exit()

full_name = " ".join(sys.argv[1:])
email = full_name.lower().replace(" ", ".") + "@deign.com"

# output
print("\n--- User Information ---")
print("Full Name:", full_name)
print("Generated Email:", email)

# Shaduling code to run at specific time
# import time
# import schedule
# def job():
#     print("Running scheduled job...")
# schedule.every(10).seconds.do(job)
# while True:
#     schedule.run_pending()
#     time.sleep(1)

