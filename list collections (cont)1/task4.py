import pandas as pd

# Creating a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Kishore', 'Diana'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)

# Using various methods
print("Head:\n", df.head(2))
print("\nTail:\n", df.tail(2))
print("\nDescribe:\n", df.describe(include='all'))
print("\nInfo:\n")
df.info()
print("\nDrop Column:\n", df.drop('City', axis=1))
print("\nFill NaN:\n", df.fillna('Unknown'))
print("\nGroup By:\n", df.groupby('City').mean())
print("\nSort Values:\n", df.sort_values(by='Age'))
print("\nMerge:\n", pd.merge(df, df, how='inner', on='Name'))
print("\nPivot Table:\n", df.pivot_table(values='Age', index='City'))
