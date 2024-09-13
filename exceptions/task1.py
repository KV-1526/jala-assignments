# Program to generate ArithmeticException without exception handling
def divide_numbers(a, b):
    result = a / b  # This will cause a ZeroDivisionError if b is 0
    print(f"The result is: {result}")

# Call the function with b = 0 to trigger the exception
divide_numbers(10, 0)
