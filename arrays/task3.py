def calculate_average(numbers):
  """Calculates the average value of an array of integers.

  Args:
    numbers: The array of integers.

  Returns:
    The average value.
  """

  if not numbers:
    return 0  # Handle empty array

  total = sum(numbers)
  average = total / len(numbers)
  return average

# Example usage:
numbers = [1, 2, 3, 4, 5]
average = calculate_average(numbers)
print("Average value:", average)