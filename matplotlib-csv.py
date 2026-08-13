import matplotlib.pyplot as plt
import csv
# Initialize empty lists
month = []
sales = []

# Read CSV file
with open('datas.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        month.append(row['Month'])
        sales.append(int(row['Sales']))

#Plot the Data
plt.plot(month, sales, marker="o")
plt.title("Monthly Sales Report")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.tight_layout()
plt.show()
