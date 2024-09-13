class Employee:
    def __init__(self, emp_id, emp_name, emp_salary, dept_id):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.dept_id = dept_id

    def __repr__(self):
        return f"Employee(emp_id={self.emp_id}, emp_name='{self.emp_name}', emp_salary={self.emp_salary}, dept_id={self.dept_id})"

# Create a list of employee objects
employees = [
    Employee(emp_id=1, emp_name="John Doe", emp_salary=1000, dept_id=1),
    Employee(emp_id=2, emp_name="Jane Smith", emp_salary=2000, dept_id=2),
    Employee(emp_id=3, emp_name="Kishore", emp_salary=1500, dept_id=3),
    Employee(emp_id=4, emp_name="Emily Davis", emp_salary=1000, dept_id=4),
    Employee(emp_id=5, emp_name="Michael Brown", emp_salary=3000, dept_id=1),
    Employee(emp_id=6, emp_name="Kishore", emp_salary=2500, dept_id=2),
    Employee(emp_id=7, emp_name="Sarah Wilson", emp_salary=1200, dept_id=3),
    Employee(emp_id=8, emp_name="James Johnson", emp_salary=1800, dept_id=4),
    Employee(emp_id=9, emp_name="Linda Martinez", emp_salary=1000, dept_id=1),
    Employee(emp_id=10, emp_name="Robert Lee", emp_salary=2200, dept_id=2)
]

# Print the list of employees to verify
for emp in employees:
    print(emp)
