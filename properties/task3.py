class EmployeeModel:
    def __init__(self, emp_id, emp_name, email_id, salary, is_employee_active):
        self._emp_id = emp_id
        self._emp_name = emp_name
        self._email_id = email_id
        self._salary = salary
        self._is_employee_active = is_employee_active

    @property
    def emp_id(self):
        return self._emp_id

    @emp_id.setter
    def emp_id(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("EmpId must be a positive integer.")
        self._emp_id = value

    @property
    def emp_name(self):
        return self._emp_name

    @emp_name.setter
    def emp_name(self, value):
        if not value:
            raise ValueError("EmpName cannot be empty.")
        self._emp_name = value

    @property
    def email_id(self):
        return self._email_id

    @email_id.setter
    def email_id(self, value):
        if not value or "@" not in value:
            raise ValueError("Invalid EmailId.")
        self._email_id = value

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Salary must be a non-negative number.")
        self._salary = value

    @property
    def is_employee_active(self):
        return self._is_employee_active

    @is_employee_active.setter
    def is_employee_active(self, value):
        if not isinstance(value, bool):
            raise ValueError("IsEmployeeActive must be a boolean value.")
        self._is_employee_active = value

# Creating an instance of EmployeeModel
employee = EmployeeModel(
    emp_id=1,
    emp_name="John Doe",
    email_id="john.doe@example.com",
    salary=50000.00,
    is_employee_active=True
)

# Accessing and displaying properties
print(f"Employee ID: {employee.emp_id}")
print(f"Employee Name: {employee.emp_name}")
print(f"Email ID: {employee.email_id}")
print(f"Salary: {employee.salary}")
print(f"Is Employee Active: {employee.is_employee_active}")

# Updating properties
employee.emp_name = "Jane Smith"
employee.salary = 60000.00
employee.is_employee_active = False

# Displaying updated properties
print(f"Updated Employee Name: {employee.emp_name}")
print(f"Updated Salary: {employee.salary}")
print(f"Updated Is Employee Active: {employee.is_employee_active}")

# Attempting to set invalid values
try:
    employee.emp_id = -1
except ValueError as e:
    print(f"Error: {e}")

try:
    employee.email_id = "invalid-email"
except ValueError as e:
    print(f"Error: {e}")

try:
    employee.salary = -5000
except ValueError as e:
    print(f"Error: {e}")

try:
    employee.is_employee_active = "yes"
except ValueError as e:
    print(f"Error: {e}")
