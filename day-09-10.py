# Day 9-10: Loops (for, while), break, continue

# For loop
for i in range(5):
    print(i)

# While loop
count = 0
while count < 5:
    print(count)
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
