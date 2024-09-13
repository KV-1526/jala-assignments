def print_largest(num1, num2, num3):
  """Prints the largest number among three.

  Args:
    num1: The first number.
    num2: The second number.
    num3: The third number.
  """

  largest = num1
  if num2 > largest:
    largest = num2
  if num3 > largest:
    largest = num3

  print(f"The largest number is: {largest}")

# Example usage:
num1 = 10
num2 = 5
num3 = 20
print_largest(num1, num2, num3)