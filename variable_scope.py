# python variables scope and life time
# Rules for LEGB to access variables => L (local) -> E (enclosing) -> G (global) -> B (buildin)

# Local Variable
def order():
    food = 'Curd rice'
    print("your order is :", food)

order()

# Enclosing with nested
def cart():
    discount = '10%'  #E
    def checkout():
        print('Applying discount:', discount)

    checkout()
cart()

# Global
user_id = 'kamal 123'

def homepage():
    print("Welcome:", user_id)

def profile():
    print("Welcome to the profile page:", user_id)

homepage()
profile()

# Buildin functions (length, lowercase, etc...)
# Buildin variables ()
print(__file__)
print(__name__)


# LEGB
delivery_partner = "Swiggy" #G

def hotel():
    item="Dosa" #E

    def order_now():
        quantity = 2
        print(f"Ordering {quantity} {item} using {delivery_partner}")

    order_now()
hotel()

print(delivery_partner)
print(__file__)
# 2:03:58