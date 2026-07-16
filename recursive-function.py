# Recursive Functions
# A recursive function is a function that calls itself to solve a problem by breaking it down into smaller, similar subproblems. Each recursive call works on a simpler version of the problem until it reaches a base case—a condition that stops the recursion and returns a result directly without making another recursive call.

# How Recursion Works
# Recursion works by dividing a large problem into smaller instances of the same problem. Each recursive call operates on a reduced version of the original input, gradually moving toward the base case. Think of it like Russian nesting dolls: you open one doll to find a smaller doll inside, and keep opening until you find the smallest doll that doesn't contain another.

def factorial(n): #5
    # Base case: stop the recursion
    if n == 0 or n == 1: # 5==1, 4 ==1, 3==1,2==1,1==1
        return 1
    # Recursive case: call itself with a smaller problem
    return n * factorial(n - 1) # 5 * factorial(5 - 1) 5 * 4 * 3 * 2 * 1

print(factorial(5))  # Output: 120 (5 * 4 * 3 * 2 * 1)


# Example 2
def countdown(n):
    if n == 0:
        print("🧨 Boom!")
        return
    print(n)
    countdown(n - 1)

print(countdown(10))