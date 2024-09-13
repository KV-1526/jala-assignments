# Function to convert different types to string
def convert_to_string():
    # Input: Taking an integer value and a float value
    int_value = int(input("Enter an integer value: "))
    float_value = float(input("Enter a float value: "))
    
    # Convert integer and float to string using str() function
    int_as_string = str(int_value)
    float_as_string = str(float_value)
    
    # Output the string representations
    print(f"int.ToString() - {int_as_string}")
    print(f"float.ToString() - {float_as_string}")

# Call the function
convert_to_string()
