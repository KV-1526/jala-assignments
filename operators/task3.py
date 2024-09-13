def are_numbers_equal(num1, num2):
  """Checks if two numbers are equal.

  Args:
    num1: The first number.
    num2: The second number.

  Returns:
    True if the numbers are equal, False otherwise.
  """

  return num1 == num2

# Example usage:
num1 = 10
num2 = 5

if are_numbers_equal(num1, num2):
  print("The numbers are equal.")
else:
  print("The numbers are not equal.")