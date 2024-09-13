class Employee:
    def __init__(self, name, employee_id):
        self._name = name
        self._employee_id = employee_id  # This is the internal attribute

    @property
    def employee_id(self):
        """
        Read-only property for employee_id.
        """
        return self._employee_id

    @property
    def name(self):
        """
        Property for name with getter and setter.
        """
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty.")
        self._name = value

# Creating an instance of Employee
emp = Employee("gowtham", "E12345")

# Accessing the read-only property
print(f"Employee ID: {emp.employee_id}")

# Accessing the property with getter and setter
print(f"Employee Name: {emp.name}")

# Setting the employee name
emp.name = "Jane Doe"
print(f"Updated Employee Name: {emp.name}")

# Attempting to modify the read-only property will result in an AttributeError
try:
    emp.employee_id = "E67890"
except AttributeError as e:
    print(f"Error: {e}")
