import pandas as pd

# Read JSON data file into a DataFrame
df = pd.read_json('pandas/sampledata.json')  # Read data from a JSON file

# Display the entire DataFrame
print(df)

# save DataFrame to a new JSON file
df.to_json('pandas/outputdata.json', orient='records', indent=2, lines=False)  # Write the DataFrame to a JSON file with records orientation and line-delimited format
print("DataFrame saved to 'pandas/outputdata.json'")  # Print confirmation message