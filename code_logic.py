"""Short summary: contains testcase notes or examples."""
def divide(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        return "cannot divide by Zero"

# print(divide(6,2)) #3.0