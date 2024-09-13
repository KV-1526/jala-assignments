def multiple_exceptions(a, b):
    try:
        result = a / b  # This may raise ZeroDivisionError
        print(f"Result: {result}")

        numbers = [1, 2, 3]
        print(numbers[3])  # This may raise IndexError

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    
    except IndexError:
        print("Error: List index out of range.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main execution
if __name__ == "__main__":
    multiple_exceptions(10, 0)  # This will raise ZeroDivisionError
    multiple_exceptions(10, 2)  # This will raise IndexError
