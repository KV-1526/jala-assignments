import pandas as pd

# Creating a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Kishore', 'Diana'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
    'EmpId': [101, 102, 103, 104],
    'EmpName': ['Alice', 'Bob', 'Kishore', 'Diana'],
    'EmpSalary': [50000, 60000, 70000, 80000],
    'Department': ['HR', 'Finance', 'IT', 'Marketing']
}
df = pd.DataFrame(data)

# Accessing and printing the 'EmpId' column using DataRow-like iteration
print("EmpId column:")
for index, row in df.iterrows():
    print(row['EmpId'])
