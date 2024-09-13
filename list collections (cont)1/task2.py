class DataTable:
    def __init__(self, name, columns, data):
        """
        Constructor to initialize the DataTable object.

        :param name: Name of the data table
        :param columns: List of column names
        :param data: List of rows, where each row is a list of values
        """
        self.name = name
        self.columns = columns
        self.data = data

    def __str__(self):
        """Return a string representation of the DataTable."""
        result = f"DataTable: {self.name}\n"
        result += ' | '.join(self.columns) + '\n'
        result += '-' * (len(' | '.join(self.columns)) + 2) + '\n'
        for row in self.data:
            result += ' | '.join(map(str, row)) + '\n'
        return result

# Creating a DataTable object using the constructor
table_name = "EmployeeData"
columns = ["Name", "Age", "City"]
data = [
    ["Alice", 25, "New York"],
    ["Bob", 30, "Los Angeles"],
    ["Kishore", 35, "Chicago"],
    ["Diana", 40, "Houston"]
]

data_table = DataTable(table_name, columns, data)

# Printing the DataTable
print(data_table)
