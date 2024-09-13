def contains_value(array, value):
  """Checks if an array contains a specific value.

  Args:
    array: The array to search.
    value: The value to search for.

  Returns:
    True if the array contains the value, False otherwise.
  """

  for element in array:
    if element == value:
      return True
  return False

# Example usage:
numbers = [1, 2, 3, 4, 5]
target_value = 3
if contains_value(numbers, target_value):
  print("Array contains the value.")
else:
  print("Array does not contain the value.")