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

feedback = input('Enter your feedback:')
with open('feedback-log.txt', 'a') as log:
    log.write(feedback + "\n")

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

# Exception handling
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Done")

