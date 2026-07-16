# Generator Functions using yield

# A generator function is a special type of function that returns an iterator object, which produces a sequence of values one at a time using the yield keyword. Instead of computing all values at once and returning them (like a regular function), generators produce values lazily—on demand—which saves memory and improves performance for large datasets.

# How Generator Functions Work
# When you call a generator function, it doesn't execute immediately. Instead, it returns a generator object. Each time you call next() on the generator or iterate through it in a loop, the function executes until it hits a yield statement, pauses, and returns the yielded value. The next time you call next(), execution resumes from where it left off.

# default use
def get_numbers1(n):
    return [i for i in range(n)]
# print(get_numbers1(10))



# example 1 for yield
def count_up_to(n):
    current = 1
    while current <= n:
        yield current  # Pause here and return current
        current += 1

# Create a generator object
gen = count_up_to(3)

# print(next(gen))  # Output: 1
# print(next(gen))  # Output: 2
# print(next(gen))  # Output: 3

# Or use it in a loop
for value in count_up_to(3):
    print(value)  # Prints 1, 2, 3