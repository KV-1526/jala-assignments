import pandas as pd

class DataSet:
    def __init__(self, name):
        self.name = name
        self.tables = {}
    
    def add_table(self, table_name, dataframe):
        self.tables[table_name] = dataframe
    
    def get_table(self, table_name):
        return self.tables.get(table_name, None)
    
    def __repr__(self):
        return f"DataSet(name={self.name}, tables={list(self.tables.keys())})"

# Creating DataFrames
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

# Creating a DataSet instance with name 'MyDataSet'
my_data_set = DataSet(name='MyDataSet')

# Adding DataFrames to the DataSet
my_data_set.add_table('Employees', df_employees)
my_data_set.add_table('Salaries', df_salaries)

# Printing the DataSet
print(my_data_set)

# Accessing and printing the tables
print("\nEmployees DataFrame:")
print(my_data_set.get_table('Employees'))

print("\nSalaries DataFrame:")
print(my_data_set.get_table('Salaries'))
