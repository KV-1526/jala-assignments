def divide_numbers(a, b):
    try:
        result = a / b
        print(f"The result of division is: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    finally:
        print("This will always execute, regardless of whether an exception occurred.")

# Main execution
if __name__ == "__main__":
    print("Example with division by zero:")
    divide_numbers(10, 0)  # This will trigger a ZeroDivisionError

    print("\nExample with valid division:")
    divide_numbers(10, 2)  # This will perform a valid division
