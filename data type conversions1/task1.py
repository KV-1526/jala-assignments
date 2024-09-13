# Function to demonstrate implicit type conversion
def implicit_type_conversion():
    # Input: Taking an integer value from the user
    int_value = int(input("Enter an integer value: "))
    
    # Python automatically handles large integers, treating them like 'long' (from Python 2)
    long_value = int_value  # In Python 3, int and long are the same type
    
    # Output the values
    print(f"Int value: {int_value}")
    print(f"Long value (handled automatically in Python): {long_value}")

# Call the function
implicit_type_conversion()
