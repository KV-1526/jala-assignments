import pandas as pd

# Creating a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Kishore', 'Diana'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)

# Accessing various properties
print("Columns:", df.columns)
print("Index:", df.index)
print("Shape:", df.shape)
print("Size:", df.size)
print("Data Types:", df.dtypes)
print("Head:\n", df.head(2))
print("Tail:\n", df.tail(2))
print("Describe:\n", df.describe(include='all'))
print("Info:\n")
df.info()
print("Values:\n", df.values)
