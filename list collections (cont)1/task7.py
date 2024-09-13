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

# Using a for loop to print the 'EmpId' column
print("EmpId column:")
for emp_id in df['EmpId']:
    print(emp_id)
