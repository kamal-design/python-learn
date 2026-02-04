# Day 19-20: List and Dictionary Comprehensions

# List comprehension
squares = [x**2 for x in range(10)]
print(squares)

# Dictionary comprehension
nums = [1, 2, 3]
square_dict = {x: x**2 for x in nums}
print(square_dict)
