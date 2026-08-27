import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log', # you can remove this line to log to console
    filemode='w'
)

def divide(a, b):
    # print(f"Dividing {a} by {b}") # development time only used
    logging.info(f"Dividing {a} by {b}")
    try:
        result = a / b
        # print(f"Result: {result}")
        logging.debug(f"Result: {result}")
        return result
    except ZeroDivisionError:
        # print("Error: Tried to divide by zero!")
        logging.error("Error: Tried to divide by zero!")
        return None

# Testing
divide(10,2)
divide(10,0)