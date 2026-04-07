def build_email(username, provider):
    if provider == 'gmail':
        return f"{username}@gmail.com"
    elif provider == 'yahoo':
        return f"{username}@yahoo.com"
    elif provider == 'hotmail':
        return f"{username}@hotmail.com"
    else:
        return f"{username}@example.com"

# Check if the script is being run as the main program
if __name__ == "__main__":
# Example usage
    print(build_email("john.doe", "gmail"))  # Output: john.doe@gmail.com
    print(build_email("jane.smith", "yahoo"))  # Output: jane.smith@yahoo.com
    print(build_email("alice", "hotmail"))  # Output: alice@hotmail.com
    print(build_email("bob", "example"))  # Output: bob@example.com


# Higher order functions (HOF) Take anotehr function as an argument or return a function as a output. hot_kindhof.py is an example of HOF. It takes a function as an argument and returns a function as a output. It is used to make code more flexible and reusable, and dynamic. They allow you to abstract away common patterns of computation and create more concise and expressive code.

# HOF is returning a function as an output. It is used to make code more flexible and reusable, and dynamic. They allow you to abstract away common patterns of computation and create more concise and expressive code. hof_return_fn.py is an example of HOF. It takes a function as an argument and returns a function as a output. It is used to make code more flexible and reusable, and dynamic. They allow you to abstract away common patterns of computation and create more concise and expressive code.

# HOFs are a fundamental concept in functional programming and are widely used in Python. They allow you to create higher-level abstractions and can lead to more elegant and efficient code. Some common examples of HOFs in Python include `map()`, `filter()`, and `reduce()`, which are used for applying functions to collections of data.