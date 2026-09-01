import pandas as pd

"""
# create a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

df = pd.DataFrame(data)
# print(df)
# print(df.dtypes)  # Display the data types of each column
# print(df['Name'])  # Selecting a single column
# print(df[['Name', 'Age']])  # Selecting specific columns
"""

df = pd.read_csv('datas.csv')  # Read data from a CSV file
# print(df)  # Display the entire DataFrame
# print(df.info())  # Display summary information about the DataFrame
# print(df.describe())  # Display statistical summary of numerical columns
print(df["Month"])  # Display the 'Month' column
# print(df.head())  # Display the first few rows of the DataFrame
# df.to_csv('output.csv', index=False)  # Write the DataFrame to a CSV file without the index
df['Month'].to_csv('pandas/dataoutput.csv', index=False)  # Write only the 'Month' column to a CSV file without the index