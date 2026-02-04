# Day 7-8: Conditional Statements (if, elif, else)

x = 10
y = 20
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x and y are equal")

# Nested if
num = 5
if num > 0:
    print("Positive number")
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
else:
    print("Non-positive number")
