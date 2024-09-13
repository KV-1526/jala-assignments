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

# New records to be added
new_records = [
    {'Name': 'Eve', 'Age': 28, 'City': 'San Francisco', 'EmpId': 105, 'EmpName': 'Eve', 'EmpSalary': 55000, 'Department': 'HR'},
    {'Name': 'Frank', 'Age': 33, 'City': 'Seattle', 'EmpId': 106, 'EmpName': 'Frank', 'EmpSalary': 65000, 'Department': 'Finance'},
    {'Name': 'Grace', 'Age': 29, 'City': 'Austin', 'EmpId': 107, 'EmpName': 'Grace', 'EmpSalary': 72000, 'Department': 'IT'},
    {'Name': 'Hannah', 'Age': 38, 'City': 'Dallas', 'EmpId': 108, 'EmpName': 'Hannah', 'EmpSalary': 83000, 'Department': 'Marketing'},
    {'Name': 'Ivy', 'Age': 27, 'City': 'San Diego', 'EmpId': 109, 'EmpName': 'Ivy', 'EmpSalary': 57000, 'Department': 'HR'}
]

# Creating a DataFrame for new records
new_df = pd.DataFrame(new_records)

# Concatenating the original DataFrame with the new records
df = pd.concat([df, new_df], ignore_index=True)

# Printing the updated DataFrame
print(df)
