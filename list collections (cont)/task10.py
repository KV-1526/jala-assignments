import pandas as pd

# Creating a new DataFrame with 5 columns and 4 records
data = {
    'ProductID': [201, 202, 203, 204],
    'ProductName': ['Laptop', 'Smartphone', 'Tablet', 'Smartwatch'],
    'Price': [1200, 800, 500, 200],
    'Stock': [15, 30, 25, 10],
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Electronics']
}

# Create the DataFrame
df_new = pd.DataFrame(data)

# Printing the DataFrame
print(df_new)
