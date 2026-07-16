# callback Function
# A callback function is a function that you pass as an argument to another function, which then calls (executes) that function at a later time or in response to a specific event. Callbacks are fundamental to asynchronous programming and event-driven architectures in Python.

#How Callbacks Work
# When you pass a function to another function, you're giving that function instructions to "call back" to your code at an appropriate moment. The receiving function doesn't know the details of what your callback does—it just knows when and how to invoke it. This creates a flexible, decoupled design where functions can communicate without being tightly bound together.

# A function that accepts a callback
def process_data(data, callback):
    result = data * 2
    callback(result)  # "Call back" to the callback function

# Define a callback function
def display_result(value):
    print(f"The result is: {value}")

# Pass the callback function as an argument
process_data(5, display_result)  # Output: The result is: 10


# example 2
def onbutton_click(callback): #show_message
    print("Button clicked") # once this print got executed
    callback()

def show_message():
    print("👋 hellow kamal, welcome")

onbutton_click(show_message)