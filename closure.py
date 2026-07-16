# closure
# A closure is a function that "remembers" and has access to variables from the scope in which it was defined, even after that outer function has finished executing. This is one of Python's powerful features for creating flexible, reusable code.

# example 1:
def outer(x):
    def inner(y):
        return x + y  # inner() accesses x from outer's scope
    return inner

add_five = outer(5)
print(add_five(3))  # Output: 8

# example 2:
def outerFn(msg):
    def innerFn():
        return f"message is:{msg}"
    return innerFn

say_hi = outerFn("Yesterday da mapla")
print(say_hi())