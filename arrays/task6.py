def copy_array(source_array):
  """Copies an array to a new array.

  Args:
    source_array: The array to copy.

  Returns:
    A copy of the source array.
  """

  return source_array.copy()

# Example usage:
original_array = [1, 2, 3, 4, 5]
copied_array = copy_array(original_array)
print(copied_array)