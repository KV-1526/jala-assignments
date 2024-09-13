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

# Creating the first instance of EmployeeModel
employee1 = EmployeeModel(
    emp_id=1,
    emp_name="John Doe",
    email_id="john.doe@example.com",
    salary=50000.00,
    is_employee_active=True
)

# Printing property values for the first instance
print("Employee 1:")
print(f"Employee ID: {employee1.emp_id}")
print(f"Employee Name: {employee1.emp_name}")
print(f"Email ID: {employee1.email_id}")
print(f"Salary: {employee1.salary}")
print(f"Is Employee Active: {employee1.is_employee_active}")

# Creating another instance of EmployeeModel with different values
employee2 = EmployeeModel(
    emp_id=2,
    emp_name="Alice Smith",
    email_id="alice.smith@example.com",
    salary=75000.50,
    is_employee_active=False
)

# Printing property values for the second instance
print("\nEmployee 2:")
print(f"Employee ID: {employee2.emp_id}")
print(f"Employee Name: {employee2.emp_name}")
print(f"Email ID: {employee2.email_id}")
print(f"Salary: {employee2.salary}")
print(f"Is Employee Active: {employee2.is_employee_active}")
