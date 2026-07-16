# Composed Function
# Function composition is a functional programming technique where you combine multiple functions to create a new function. The result of one function becomes the input to the next, allowing you to build complex operations from simpler, reusable building blocks.

# In mathematics, function composition is written as (f∘g)(x)=f(g(x)), meaning you apply function g first, then apply function f to the result. Python doesn't have built-in composition syntax, but you can easily create composed functions manually or with helper utilities.

# Simple functions to compose
def add_five(x):
    return x + 5

def multiply_by_two(x):
    return x * 2

# Manual composition
def compose(f, g):
    def composed(x):
        return f(g(x))
    return composed

# Create a composed function: first multiply by 2, then add 5
result_func = compose(add_five, multiply_by_two)

print(result_func(3))  # Output: 11 (3 * 2 = 6, then 6 + 5 = 11)