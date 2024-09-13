class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def get_employee_details(self):
        print("Employee ID:", self.id)
        print("Employee Name:", self.name)
        print("Employee Salary:", self.salary)

# Create an instance of the Employee class
employee1 = Employee(101, "gowtham", 50000)

# Get and print employee details
employee1.get_employee_details()