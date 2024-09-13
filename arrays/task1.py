def sum_of_integers(numbers):
  """Calculates the sum of integer values in an array.

  Args:
    numbers: The array of integers.

  Returns:
    The sum of the integers.
  """

  total = 0
  for num in numbers:
    total += num
  return total

# Example usage:
numbers = [1, 2, 3, 4, 5]
sum = sum_of_integers(numbers)
print("Sum of integers:", sum)