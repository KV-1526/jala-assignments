def arithmetic_operations(num1, num2):
  """Performs arithmetic operations on two numbers.

  Args:
    num1: The first number.
    num2: The second number.

  Returns:
    A dictionary containing the results of the arithmetic operations.
  """

  results = {
      "addition": num1 + num2,
      "subtraction": num1 - num2,
      "multiplication": num1 * num2,
      "division": num1 / num2 if num2 != 0 else "Cannot divide by zero"
  }

  return results

# Example usage:
num1 = 10
num2 = 5
result = arithmetic_operations(num1, num2)
print(result)