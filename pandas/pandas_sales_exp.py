import pandas as pd
# step1: read the data from csv file
df = pd.read_csv('pandas/salesdata.csv')  # Read data from a CSV file

# step2: Add New columns - Total, Gross Profit, Profit Margin
df['Total'] = df['Units'] * df['Unit_Price']  # Calculate Total sales

# step3: Group by a specific column (e.g., 'Product')
grouped = df.groupby('Product')['Total'].sum().reset_index()

# step4: Sort the grouped data by Total in descending order
sorted_grouped = grouped.sort_values(by='Total', ascending=False)

# step5: Calculate Gross Profit and Profit Margin
df['Gross Profit'] = df['Total'] - df['Unit_Price']
df['Profit Margin'] = (df['Gross Profit'] / df['Total']) * 100

# step6: Save the modified DataFrame to a new CSV file
df.to_csv('pandas/modified_salesdata.csv', index=False)  # Write the modified DataFrame
print("Modified sales data saved to 'pandas/modified_salesdata.csv'")
print(sorted_grouped)  # Display the sorted grouped data
print('\n\n')
print(pd.read_csv('pandas/modified_salesdata.csv'))