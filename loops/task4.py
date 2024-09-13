def print_odd_even(num):
  """Prints whether a number is odd or even.

  Args:
    num: The number to check.
  """

  if num % 2 == 0:
    print(f"{num} is even.")
  else:
    print(f"{num} is odd.")

# Example usage:
num = 15
print_odd_even(num)