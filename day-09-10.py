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
    print(i)
