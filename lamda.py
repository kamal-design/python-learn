# lambda argument_: expression
# map, filter, reduce

# map (funcation, iterable)
# reduce (funcation, iterable)

from functools import reduce

add = lambda a, b : a + b
print(add(1,5)) #output: 6

square = lambda x : x*x
print(square(2)) #output: 4

fruits = ['apple', 'banana', 'mango']
result = list(map(lambda fruit: fruit.upper(), fruits))
print(result)

nums = [1,2,3,4,5,6]
even = list(filter(lambda x : x%2 == 0, nums))
print(even) # 4/2 reminder 0 => [2, 4, 6]

total = reduce(lambda a,b : a+b, nums)
print(total) #output 21

num_max =[ 10, 24, 33, 5, 7]
maxi = reduce(lambda a,b : a if a > b else b, num_max)
print(maxi) #output 33


# real time example
prices = [250, 900, 1200, 400, 1500]
expesive = list(filter(lambda x: x > 1000, prices))
grandTotal = reduce(lambda a,b: a+b, expesive)
print(grandTotal) # 1200, 1500 => 2700