def natural_numbers_and_sum(n):
  """Displays the first n natural numbers and their sum.

  Args:
    n: The number of natural numbers to display.
  """

  numbers = []
  sum = 0

  for i in range(1, n + 1):
    numbers.append(i)
    sum += i

  print("The first", n, "natural numbers are:")
  print(numbers)
  print("The sum of natural numbers up to", n, "terms:", sum)

# Get user input
n = int(input("Enter the number of natural terms you want: "))

# Display the natural numbers and their sum
natural_numbers_and_sum(n)