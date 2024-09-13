def print_smaller_and_larger(num1, num2):
  """Prints the smaller and larger numbers.

  Args:
    num1: The first number.
    num2: The second number.
  """

  if num1 < num2:
    smaller = num1
    larger = num2
  else:
    smaller = num2
    larger = num1

  print(f"Smaller number: {smaller}")
  print(f"Larger number: {larger}")

# Example usage:
num1 = 10
num2 = 5
print_smaller_and_larger(num1, num2)