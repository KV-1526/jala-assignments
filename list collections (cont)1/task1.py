import pandas as pd

# Creating a dictionary with data
data = {
    'Name': ['Alice', 'Bob', 'Kishore', 'Diana'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

# Creating a DataFrame from the dictionary
df = pd.DataFrame(data)

# Printing the DataFrame
print(df)
