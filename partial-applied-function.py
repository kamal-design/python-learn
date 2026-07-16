# partial applied function
# Partial application is a functional programming technique where you fix some arguments of a function, creating a new function with fewer parameters. In Python, this is typically implemented using the functools.partial() function, which creates what's called a partial function or partially applied function.
from functools import partial

# example normal calculation step 1
def calculate_Price(basePrice, taxRate):
    return basePrice * (1 + taxRate)

print(calculate_Price(1000,0.18)) # 1180.0
print(calculate_Price(500, 0.18)) # 590.0


# A Practical Example
# step 2
price_with_gst = partial(calculate_Price, taxRate = 0.18)

# step3 now use it without passing tac_rate again
print(price_with_gst(1000)) # 1180.0
print(price_with_gst(500)) # 590.0

def multiply(x, y):
    return x * y

# Create a partial function that multiplies by 2
double = partial(multiply, 2)

print(double(5))   # Output: 10
print(double(10))  # Output: 20


# Gmail Creation using partial
def create_email(userName, domain):
    return f"{userName}@{domain}"

gmail = partial(create_email, domain="gmail.com")
ymail = partial(create_email, domain="ymail.com")

print(gmail("kamal")) # kamal@gmail.com
print(ymail("rahul")) # rahul@ymail.com