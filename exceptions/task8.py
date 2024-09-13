def perform_division(a, b):
    # This function attempts to divide 'a' by 'b'
    result = a / b  # This will raise a ZeroDivisionError if 'b' is 0
    return result

# Main execution
if __name__ == "__main__":
    try:
        numerator = 10
        denominator = 0  # Setting denominator to 0 to trigger the exception
        print(f"Performing division: {numerator} / {denominator}")
        result = perform_division(numerator, denominator)
        print(f"Result of division: {result}")
    except ZeroDivisionError:
        print("Caught an exception: Division by zero is not allowed.")
