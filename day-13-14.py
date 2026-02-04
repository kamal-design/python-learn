# Day 13-14: Scope, Lambda, Map, Filter, Reduce
from functools import reduce

def outer():
    x = "local"
    def inner():
        print("Inner:", x)
    inner()
outer()

# Lambda
square = lambda x: x * x
print(square(5))

# Map
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
print(squared)

# Filter
even = list(filter(lambda x: x % 2 == 0, nums))
print(even)

# Reduce
sum_all = reduce(lambda a, b: a + b, nums)
print(sum_all)
