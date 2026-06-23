# pure function and impure functions



total = 0

def add(amount):
    # global total # inpurefuction
    total = 1  # pure function
    total += amount
    print("i and from add()", total)

# add(2)
def test():
    print("i am from test()", total)

add(2)
test()

# no value change define hotcode fun
def greet(name="kamalM"):
    print(f'Hello, {name}!')

greet()

# More pure function examples
def add_numbers(x, y):
    return x + y


def multiply_numbers(x, y):
    return x * y


def format_full_name(first, last):
    return f"{first} {last}"


# More impure function examples

message_log = []

def append_message(msg):
    message_log.append(msg)
    print("Message added:", msg)


def set_global_total(value):
    global total
    total = value
    print("Global total set to", total)


# Demonstration of the new examples

print("add_numbers(3, 5) ->", add_numbers(3, 5))
print("multiply_numbers(4, 7) ->", multiply_numbers(4, 7))
print("format_full_name('Kamal', 'M') ->", format_full_name('Kamal', 'M'))

append_message('hello from impure function')
append_message('another message')
print('message_log ->', message_log)

set_global_total(10)
test()