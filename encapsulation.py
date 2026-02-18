# Encapsulation (bundling data and methods that operate on the data together)

class Order: # constructor created
    def __init__(self, order_id, customer_name, items, total_amount, discount_amount):
        self.order_id = order_id                 #public
        self.customer_name = customer_name       #public
        self.items = items                       #public
        self.__total_amount = total_amount         #private
        self.__discount_amount = discount_amount   #private

    def __calculate_final(self): # privete helper method
        return self.__total_amount - self.__discount_amount

# created dictionaries view
    def _gat_admin_view(self): # protected method
        return {
            "Customer": self.customer_name,
            "Items": self.items,
            "Total Amount": f"₹{self.__total_amount}",
            "Discount Amount": f"₹{self.__discount_amount}",
            "Final Bill": f"₹{self.__calculate_final()}"
        }

    def _gat_customer_view(self): # public method
        return {
            "Customer": self.customer_name,
            "Items": self.items,
            "Final Bill": f"₹{self.__calculate_final()}"
        }

class AdminPortal:
    def show_order(self, order):
        return order._gat_admin_view() # protected method

class CustomerApp:
    def show_order(self, order):
        return order._gat_customer_view() # self public method

admin = AdminPortal()
customer = CustomerApp()

order = Order(1, "Kamal", ["Pizza", "Chicken Lolly pop", "Cold Drink"], 1000, 100)

# print(order.__calculate_final()) # here private method not access
print("\n\nAdmin", admin.show_order(order))
print("\n\nCustomer", customer.show_order(order))
