import pandas as pd

# Creating a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Kishore', 'Diana'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)

# Adding new columns to the DataFrame
df['EmpId'] = [101, 102, 103, 104]
df['EmpName'] = ['Alice', 'Bob', 'Kishore', 'Diana']
df['EmpSalary'] = [50000, 60000, 70000, 80000]
df['Department'] = ['HR', 'Finance', 'IT', 'Marketing']

# Printing the updated DataFrame
print(df)
