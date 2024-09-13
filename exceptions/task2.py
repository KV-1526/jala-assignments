# Program to handle ArithmeticException using try-except block
def divide_numbers(a, b):
    try:
        result = a / b  # This may raise a ZeroDivisionError
        print(f"The result is: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

# Call the function with b = 0 to handle the exception
divide_numbers(10, 0)
