import pandas as pd

# Creating multiple DataFrames to simulate a DataSet
data1 = {
    'EmployeeID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Position': ['Manager', 'Developer', 'Analyst', 'Designer']
}
df_employees = pd.DataFrame(data1)

data2 = {
    'EmployeeID': [1, 2, 3, 4],
    'Department': ['HR', 'IT', 'Finance', 'Marketing'],
    'Salary': [70000, 80000, 75000, 72000]
}
df_salaries = pd.DataFrame(data2)

# Simulating a DataSet by combining DataFrames into a dictionary
data_set = {
    'Employees': df_employees,
    'Salaries': df_salaries
}

# Printing the contents of the simulated DataSet
print("Employees DataFrame:")
print(data_set['Employees'])
print("\nSalaries DataFrame:")
print(data_set['Salaries'])
