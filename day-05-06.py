# Day 5-6: Lists, Tuples, Sets, Dictionaries

# Lists []
# lists is ordered collection of items
# lists is mutable (append, insert, remove, pop, update any item)
# list Methods (append, insert, remove, pop, count, index, sort, reverse, copy, extend)

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

# check iteration of tuple
for item in tuple1:
    print(item) # 1 2 3 1

# check length of tuple
print("Length of tuple:", len(tuple1)) # 4

# Sets (Unordered, Unique elements) {}
# set is not indexed
# set is mutable means it can be changed
# set is unordered means it cannot be ordered
# set is unique elements means it cannot have duplicate values
# set Methods (add, remove, discard, pop, clear, update, intersection, difference, symmetric_difference)
# set using mathamatical set operations (union, intersection, difference, symmetric_difference)
# set is hashable means it can be used as a key in a dictionary

set1 = {1, 2, 3, 2, 3} # Duplicates are automatically removed
print("Set:", set1) # {1, 2, 3}
set1.add(4)
print("After add(4):", set1) # {1, 2, 3, 4}
set1.remove(2)
print("After remove(2):", set1) # {1, 3, 4}
set1.discard(10) # discard doesn't error if item is missing
print("After discard(10):", set1) # {1, 3, 4}

uber_city = {"chennai", "bangalore", "hyderabad", "mumbai", "delhi"}
uber_city2 = {"goa", "pune", "mumbai", "delhi"}
print(uber_city.union(uber_city2)) # union of two sets
print(uber_city.intersection(uber_city2)) # intersection of two sets
print(uber_city.difference(uber_city2)) # difference of two sets
print(uber_city.symmetric_difference(uber_city2)) # symmetric difference of two sets
uber_city.add("coimbatore")
print("After add(coimbatore):", uber_city) # {'chennai', 'bangalore', 'hyderabad', 'mumbai', 'delhi', 'coimbatore'}
uber_city.remove("coimbatore")
print("After remove(coimbatore):", uber_city) # {'chennai', 'bangalore', 'hyderabad', 'mumbai', 'delhi'}
uber_city.discard("coimbatore")
print("After discard(coimbatore):", uber_city) # {'chennai', 'bangalore', 'hyderabad', 'mumbai', 'delhi'}
uber_city.pop()
print("After pop():", uber_city) # {'chennai', 'bangalore', 'hyderabad', 'mumbai'}
uber_city.clear()
print("After clear():", uber_city) # set()

# Dictionaries (Key-Value pairs)
person = {"name": "Arun kumar", "age": 25}
print("Dictionary:", person) # {'name': 'Arun kumar', 'age': 25}
print("Name:", person["name"]) #check key is present or not # Arun kumar
print("Age using get():", person.get("age")) #check key is present or not using get() method # 25
print('keys', person.keys()) # ['name', 'age']
print('values', person.values()) # ['Arun kumar', 25]
print('items', person.items()) # [('name', 'Arun kumar'), ('age', 25)]

# iteration of dictionary items
for key, value in person.items():
    print(key, ':', value)

person["city"] = "New York" # Add new key-value
# update is check key to update other wise add new key
person.update({"email": "arun@example.com", "age": 26}) # Update multiple
print("Updated Dictionary:", person) # {'name': 'Arun kumar', 'age': 26, 'email': arun@example.com', 'city': 'New York'}

print("Keys:", list(person.keys())) # ['name', 'age', 'email', 'city']
print("Values:", list(person.values())) # ['Arun kumar', 26, 'arun@example.com', 'New York']
print("Items:", list(person.items())) # [('name', 'Arun kumar'), ('age', 26), ('email', 'arun@example.com'), ('city', 'New York')]

trips = [
    {'trip_id':1, 'trip_name':'chennai to bangalore', 'trip_date':'2022-01-01', 'trip_amount':1000},
    {'trip_id':2, 'trip_name':'bangalore to hyderabad', 'trip_date':'2022-01-02', 'trip_amount':2000},
    {'trip_id':3, 'trip_name':'hyderabad to mumbai', 'trip_date':'2022-01-03', 'trip_amount':3000},
    {'trip_id':4, 'trip_name':'mumbai to delhi', 'trip_date':'2022-01-04', 'trip_amount':4000},
    {'trip_id':5, 'trip_name':'delhi to chennai', 'trip_date':'2022-01-05', 'trip_amount':5000}
]

# iteration of list of dictionaries
for trip in trips:
    print(trip["trip_name"])

trips_dict = {
    'T001': {'trip_id':'T001', 'trip_name':'chennai to bangalore', 'trip_date':'2022-01-01', 'trip_amount':1000},
    'T002': {'trip_id':'T002', 'trip_name':'bangalore to hyderabad', 'trip_date':'2022-01-02', 'trip_amount':2000},
    'T003': {'trip_id':'T003', 'trip_name':'hyderabad to mumbai', 'trip_date':'2022-01-03', 'trip_amount':3000},
    'T004': {'trip_id':'T004', 'trip_name':'mumbai to delhi', 'trip_date':'2022-01-04', 'trip_amount':4000},
    'T005': {'trip_id':'T005', 'trip_name':'delhi to chennai', 'trip_date':'2022-01-05', 'trip_amount':5000}
}
print(trips_dict["T001"]["trip_name"])

for trip_id, trip_info in trips_dict.items():
    print(trip_id, trip_info["trip_name"])
    print(trip_info['trip_id'], '-->', trip_info["trip_name"])


# pop is remove last value and return it
# use pop('args') to remove and return the value of the key 'city'
removed_value = person.pop("city") # remove and return the value of the key 'city'
print("After pop('city'):", person, "| Removed:", removed_value) # {'name': 'Arun kumar', 'age': 26, 'email': 'arun@example.com'} | Removed: New Yorkt


# list slicing
# list[start:end:step]

play_list = ['song1', 'song2', 'song3', 'song4', 'song5']
print("Play List:", play_list) # ['song1', 'song2', 'song3', 'song4', 'song5']
print("Play List Slicing:", play_list[0:4]) # ['song1', 'song2', 'song3', 'song4']
print("Play List Slicing:", play_list[0:4:2]) # ['song1', 'song3']

# list iteration
for song in play_list:
    print('song name:', song)

# list iteration with index using enumerate
for index, song in enumerate(play_list):
    print('index:', index + 1, 'song name:', song)

# list check if item is in list
print("Play List:", play_list)
if "song2" in play_list:
    print("song2 is in play_list")
else:
    print("song2 is not in play_list")

# list check if item is not in list
print("Play List:", play_list)
if "song6" not in play_list:
    print("song6 is not in play_list")
else:
    print("song6 is in play_list")

# list update
play_list[1] = "khatal kanave"
print("Play List:", play_list)

# list mixed data types
play_list = ['song1', 'song2', 'song3', 'song4', 'song5', 1, 2, 3, 4, 5, True, False]
print("Play List:", play_list)

# list use key value pairs
play_list = {'song': 'khatal kanave', 'Movie': 'Moondasu patti', 'Actor': 'Vishnu vishal', 'Award': 'Best Actor and Movie', 'Year': '2015'}

print("Play List:", play_list)

