def remove_element(array, value):
  """Removes the first occurrence of a specific value from an array.

  Args:
    array: The array to modify.
    value: The value to remove.

  Returns:
    The modified array.
  """

  index = array.index(value) if value in array else None
  if index is not None:
    del array[index]
  return array

# Example usage:
numbers = [1, 2, 3, 4, 5, 3]
removed_array = remove_element(numbers, 3)
print(removed_array)