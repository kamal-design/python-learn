# Day 7-8: Conditional Statements (if, elif, else)
# Match Case - Similar to switch-case
# and, or, not operators

x = 10
y = 20
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x and y are equal")

# Nested if
num = 5 # or 4
if num > 0:
    print("Positive number")
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
else:
    print("Non-positive number")

# Truthy and Falsy Values
# Falsy values: 0, 0.0, "", [], {}, (), None, False
# Everything else is Truthy
name = ""
if not name:
    print("Name is empty (Falsy)")

items = [1, 2]
if items:
    print("List has items (Truthy)")

# Match Case (Python 3.10+) - Similar to switch-case in other languages
status = 404
match status:
    case 200:
        print("Success")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("Unknown Status")

# conditionals
age = 30
if age >= 18:
    print("you can vote")
else:
    print("you can't vote")

# student marks system
marks = 90
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
elif marks >= 50:
    print("Grade E")
else:
    print("Fail")

# Nested if condition
driver_age = 20 # 18 or above
driver_license = 'yes' # yes or no
driver_license_valid = True # True or False

if driver_age >= 18:
    if driver_license == 'yes' and driver_license_valid == True:
        print("you can drive")
    else:
        print("you don't have license. go and take license or check your license validity")
else:
    print("you can't drive")

# Example of nested if condition
marks = 85
attendance = 60 # 80 or above

# and condition
if marks >= 50 and attendance >= 60:
    print("you can allowed for exam")
else:
    print("you can't allowed for exam")

# or condition
if marks >= 50 or attendance >= 80:
    print("you can allowed for exam")
else:
    print("you can't allowed for exam")

# Example of nested if condition for mobile recharge
recharge_amount = 349
data_limit = 2 # GB
internet_pack = '5G' # or 4G

if recharge_amount >= 399 and data_limit >= 2 and internet_pack == '5G':
    print("you can use mobile and internet 5G user")
else:
    print("you can't use mobile and internet 5G user") # result condition false

# or condition
if recharge_amount >= 349 or data_limit >= 2:
    print("you can use mobile and internet") # result condition true
else:
    print("you can't use mobile and internet")

# not condition
if not (recharge_amount >= 349 or data_limit >= 2):
    print("you can't use mobile and internet")

# hotel
order_amount = 1000
days = 'Saturday' # or 'Sunday'
membership_card = 'Gold' # silver, platinum, diamond

if (order_amount >= 1000 and days in ['Saturday','Sunday']) or membership_card == 'Gold':
    print("you can get free delivery and 20% discount") # result condition true
else:
    print("you can't get free delivery and no discount")


days = 'Monday' # day changed
membership_card = 'Silver' # changed to Silver to test non-eligibility
if (order_amount >= 1000 and days in ['Saturday','Sunday']) or membership_card == 'Gold':
    print("you can get free delivery and 20% discount")
else:
    # This will now trigger because it's Monday AND not a Gold member
    print("you can't get free delivery and no discount")


#