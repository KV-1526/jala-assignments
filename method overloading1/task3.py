def sum_values(numbers):
  """Calculates the sum of a list of numbers.

  Args:
    numbers: A list of numbers to add.

  Returns:
    The sum of the numbers.
  """

  total = 0
  for num in numbers:
    total += num
  return total

# Get user input
numbers_input = input("Enter numbers separated by spaces: ")
numbers = [int(num) for num in numbers_input.split()]

# Calculate and print the sum
sum_result = sum_values(numbers)
print("The sum of the numbers is:", sum_result)