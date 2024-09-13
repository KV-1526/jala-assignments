def get_difference(array):
  """Calculates the difference between the largest and smallest values in an array.

  Args:
    array: The array to analyze.

  Returns:
    The difference between the largest and smallest values.
  """

  if not array:
    raise ValueError("Array is empty")

  min_value = max_value = array[0]

  for num in array:
    if num < min_value:
      min_value = num
    if num > max_value:
      max_value = num

  return max_value - min_value

# Example usage:
numbers = [1, 2, 3, 4, 5, 100, -10]
difference = get_difference(numbers)
print("Difference between largest and smallest values:", difference)