# Function to demonstrate built-in type conversion methods
def built_in_type_conversion():
    # Input: Taking a string that represents a float value and an integer value
    string_name = input("Enter a string representing a float value: ")
    int_value = int(input("Enter an integer value: "))
    
    # Convert the string to a float
    float_value = float(string_name)
    
    # In Python, float is equivalent to double in other languages, so we just output the integer
    # Convert the integer to "double" (which is represented by float)
    double_value = float(int_value)
    
    # Output the converted values
    print(f"String to float: {float_value}")
    print(f"Int to double (float): {double_value}")

# Call the function
built_in_type_conversion()
