def odd_natural_numbers_and_sum(n):
  """Displays the first n odd natural numbers and their sum.

  Args:
    n: The number of odd natural numbers to display.
  """

  numbers = []
  sum = 0

  for i in range(1, 2 * n, 2):
    numbers.append(i)
    sum += i

  print("The odd numbers are:", numbers)
  print("The sum of odd natural numbers up to", n, "terms:", sum)

# Get user input
n = int(input("Input number of terms: "))

# Display the odd natural numbers and their sum
odd_natural_numbers_and_sum(n)