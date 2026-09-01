import pandas as pd

# create a DataFrame from a dictionary
# Customers Table
customers = pd.DataFrame({
    'CustomerID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
})

# Order Table
orders = pd.DataFrame({
    'OrderID': [101, 102, 103, 104],
    'CustomerID': [1, 2, 1, 3],
    'Product': ['Laptop', 'Smartphone', 'Tablet', 'Headphones'],
    'Amount': [1200, 800, 300, 150]
})

# Perform an inner join on the 'CustomerID' column
result = pd.merge(customers, orders, on='CustomerID', how='inner')
print("Inner Join Result:\n", result)

# Apply a filter to get customers from 'New York'
ny_customers = customers[customers['City'] == 'New York']
print("\nCustomers from New York:\n", ny_customers)

# Apply a filter to get orders with an age greater than 0 to 35
orders_with_age_filter = pd.merge(customers[(customers['Age'] > 0) & (customers['Age'] <= 35)], orders, on='CustomerID', how='inner')
print("\nOrders with Customers Age 0-35:\n", orders_with_age_filter)

# Filter
newDatas = pd.DataFrame({'x': [1,2,3,4,5]})
result = newDatas[newDatas['x'] > 3 ] # this will filter the data and return only the rows where the value of 'x' is greater than 3
print("\nFiltered Data (x > 3):\n", result)

# specify header columns name
df = pd.read_csv('pandas/noheader.csv', header=None, names=['Name', 'Age', 'Designation'])
print("\nDataFrame with Specified Header Columns:\n", df)