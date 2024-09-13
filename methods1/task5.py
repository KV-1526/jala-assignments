def print_even_numbers(n):
  """Prints the first n even numbers.

  Args:
    n: The number of even numbers to print.
  """

  for i in range(2, 2 * n + 2, 2):
    print(i, end=" ")

# Get user input
n = int(input("Enter a number: "))

# Print the even numbers
print_even_numbers(n)