# Day 5-6: Lists, Tuples, Sets, Dictionaries

# Lists
fruits = ["apple", "banana", "cherry"]
print("Original list:", fruits) # ['apple', 'banana', 'cherry']

fruits.append("orange") # add orange to the end
print("After append:", fruits) # ['apple', 'banana', 'cherry', 'orange']

print("Item at index 1:", fruits[1]) # banana

fruits.insert(1, "Guava") # insert guava at index 1
print("After insert:", fruits) # ['apple', 'Guava', 'banana', 'cherry', 'orange']

fruits.remove("Guava") # remove guava from the list
print("After remove:", fruits) # ['apple', 'banana', 'cherry', 'orange']

removed_item = fruits.pop() # remove and return last item
print("After pop():", fruits, "| Removed:", removed_item) # ['apple', 'banana', 'cherry'] | orange

removed_at_index = fruits.pop(1) # remove and return item at index 1
print("After pop(1):", fruits, "| Removed:", removed_at_index) # ['apple', 'cherry'] | banana

# Reset the list for further demonstrations
fruits = ["apple", "banana", "cherry", "apple"]
print("Reset list for demo:", fruits)

apple_count = fruits.count("apple") # count occurrences
print("Count of 'apple':", apple_count) # 2

apple_index = fruits.index("apple") # find first index of 'apple'
print("Index of first 'apple':", apple_index) # 0

fruits.sort() # sort the list alphabetically
print("After sort:", fruits) # ['apple', 'apple', 'banana', 'cherry']

fruits.reverse() # reverse the current order
print("After reverse:", fruits) # ['cherry', 'banana', 'apple', 'apple']

fruits_copy = fruits.copy() # create a shallow copy
print("Copy of list:", fruits_copy)

fruits.extend(["orange", "mango"]) # add multiple items
print("After extend:", fruits) # ['cherry', 'banana', 'apple', 'apple', 'orange', 'mango']

# remove duplicats here
print('Removed Duplicates:', list(set(fruits))) # ['cherry', 'banana', 'apple', 'orange', 'mango']

# Note: .sort() modifies the list in-place and returns None.
# Use sorted() to return a new sorted list for printing.
print('Order List:', sorted(list(set(fruits)))) # ['apple', 'banana', 'cherry', 'mango', 'orange']

fruits.clear() # remove all items
print("After clear:", fruits) # []




# Tuples (Immutable)
# tuple is immutable means it cannot be changed
# tuple is ordered
# tuple is indexed
# tuple is iterable
# tuple is hashable
# tuple is count
# tuple is index

tuple1 = (1, 2, 3, 1)
print("Tuple:", tuple1) # (1, 2, 3, 1)
print("First element:", tuple1[0]) # 1

# check .count(x) of 1 in tuple Since it found the number 1 twice, tuple1.count(1) returns 2.
print("Count of 1:", tuple1.count(1)) # 2
# check .index(x) of 2 in tuple Since it found the number 2 at the second position (index 1), tuple1.index(2) returns 1.
print("Index of 2:", tuple1.index(2)) # 1




# Sets (Unordered, Unique elements)
set1 = {1, 2, 3, 2, 3} # Duplicates are automatically removed
print("Set:", set1) # {1, 2, 3}
set1.add(4)
print("After add(4):", set1) # {1, 2, 3, 4}
set1.remove(2)
print("After remove(2):", set1) # {1, 3, 4}
set1.discard(10) # discard doesn't error if item is missing
print("After discard(10):", set1) # {1, 3, 4}



# Dictionaries (Key-Value pairs)
person = {"name": "Arun kumar", "age": 25}
print("Dictionary:", person) # {'name': 'Arun kumar', 'age': 25}
print("Name:", person["name"]) # Arun kumar
print("Age using get():", person.get("age")) # 25

person["city"] = "New York" # Add new key-value
person.update({"email": "arun@example.com", "age": 26}) # Update multiple
print("Updated Dictionary:", person) # {'name': 'Arun kumar', 'age': 26, 'email': arun@example.com', 'city': 'New York'}

print("Keys:", list(person.keys())) # ['name', 'age', 'email', 'city']
print("Values:", list(person.values())) # ['Arun kumar', 26, 'arun@example.com', 'New York']
print("Items:", list(person.items())) # [('name', 'Arun kumar'), ('age', 26), ('email', 'arun@example.com'), ('city', 'New York')]

removed_value = person.pop("city") # remove and return the value of the key 'city'
print("After pop('city'):", person, "| Removed:", removed_value) # {'name': 'Arun kumar', 'age': 26, 'email': 'arun@example.com'} | Removed: New York
