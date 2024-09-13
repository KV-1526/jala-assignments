# Function to demonstrate relational operators
def relational_operations(a, b):
    # Equal to (==)
    print(f"Equal to Operator: {a == b}")
    
    # Greater than (>)
    print(f"Greater than Operator: {a > b}")
    
    # Less than (<)
    print(f"Less than Operator: {a < b}")
    
    # Greater than or equal to (>=)
    print(f"Greater than or Equal to Operator: {a >= b}")
    
    # Less than or equal to (<=)
    print(f"Lesser than or Equal to Operator: {a <= b}")
    
    # Not equal to (!=)
    print(f"Not Equal to Operator: {a != b}")

# Input from user
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))

# Call the function
relational_operations(a, b)
