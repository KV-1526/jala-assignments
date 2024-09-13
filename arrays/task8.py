def find_min_max(array):
  """Finds the minimum and maximum values in an array.

  Args:
    array: The array to search.

  Returns:
    A tuple containing the minimum and maximum values.
  """

  if not array:
    raise ValueError("Array is empty")

  min_value = max_value = array[0]
  for num in array:
    if num < min_value:
      min_value = num
    if num > max_value:
      max_value = num

  return min_value, max_value

# Example usage:
numbers = [1, 2, 3, 4, 5, 100, -10]
min_num, max_num = find_min_max(numbers)
print("Minimum value:", min_num)
print("Maximum value:", max_num)