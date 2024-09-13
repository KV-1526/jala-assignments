class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary  # This is the internal attribute

    @property
    def name(self):
        """
        Property to get the employee's name.
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        Property setter to set the employee's name with validation.
        """
        if not value:
            raise ValueError("Name cannot be empty.")
        self._name = value

    @property
    def salary(self):
        """
        Property to get the employee's salary.
        """
        return self._salary

    @salary.setter
    def salary(self, value):
        """
        Property setter to set the employee's salary with validation.
        """
        if value < 0:
            raise ValueError("Salary cannot be negative.")
        self._salary = value

# Creating an instance of Employee
emp = Employee("John Doe", 50000)

# Accessing and displaying the properties
print(f"Employee Name: {emp.name}")
print(f"Employee Salary: {emp.salary}")

# Updating the properties
emp.name = "Jane Smith"
emp.salary = 60000

# Displaying updated properties
print(f"Updated Employee Name: {emp.name}")
print(f"Updated Employee Salary: {emp.salary}")

# Attempting to set invalid values
try:
    emp.name = ""
except ValueError as e:
    print(f"Error: {e}")

try:
    emp.salary = -1000
except ValueError as e:
    print(f"Error: {e}")
