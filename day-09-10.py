# Day 9-10: Loops (for, while), break, continue

# For loop
for i in range(5):
    print('For loop:',i)

# While loop
count = 0
while count < 5:
    print('While loop:',count)
    count += 1

# Break and continue
for i in range(10):
    if i == 7:
        break
    if i % 2 == 0:
        continue
    print("Looping:", i)

# Loop with Enumerate (Gets index and value)
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# Zip (Loop through two lists at once)
prices = [10, 20, 30]
for fruit, price in zip(fruits, prices):
    print(f"The {fruit} costs ${price}")

# for loop different this run entire list or array for looping (for each no condition check use if or else)
names = ['saravanan', 'kamal', 'karthik', 'suresh', 'kumar', 'balamani', 'arun']
for name in names:
    print(name.upper())

# while loop is condition based loop again and again run until condition is true
# break is used to exit the loop
# continue is used to skip the current iteration
# pass is used to do nothing (placeholder)

# for loop is used to iterate over a sequence (list, tuple, string, etc..)
# while loop is used to iterate over a sequence (list, tuple, string, etc..) until the condition is true

atm_pin = 1234
enter_pin = None

while enter_pin != atm_pin:
    enter_pin = int(input("Enter your PIN: "))
    print("Correct PIN your free to use atm")

print("Incorrect PIN try again")

# for loop check nummer

numInputs = [1,2,3,4, 8,6,9,7,10,5]
for i in numInputs:
    if i == 5:
        break
    print("input numbers:", i) # 5 is not printed because break is used

# for loop check number

numInputs = [1,2,3,4, 8,6,9,7,10,5]
for i in numInputs:
    if i == 5:
        continue
    print("loop continue:", i) # 5 is not printed because continue is used

# for loop check number

numInputs = [1,2,3,4, 8,6,9,7,10,5]
for i in numInputs:
    if i == 5:
        pass
    print("loop pass:", i) # 5 is not printed because pass is used

numInputs = [1,2,3,4, -1,-3, -5, -7, 8,6,9,7,10,5]
for i in numInputs:
    if i < 0:
        continue
    print("loop pasitive num:", i) # 5 is not printed because continue is used

# coundtown timer

import time

for i in range(10, 0, -1):
    print(i)
    time.sleep(1)
print("Blast")

# while loop example
count = 5
while count > 0:
    print(f"coundtown : {count}")
    count -= 1
print("Blast")

# shopping card example
items = []
while True:
    item = input("Add item (type 'done' to finish): ")
    if item == "done":
        break
    items.append(item)
print("items in card: ", items)