def find_common_values(array1, array2):
  """Finds common values between two arrays.

  Args:
    array1: The first array.
    array2: The second array.

  Returns:
    A list of common values.
  """

  common_values = []
  set1 = set(array1)
  set2 = set(array2)

  for value in set1:
    if value in set2:
      common_values.append(value)

  return common_values

# Example usage:
array1 = [1, 2, 3, 4, 5]
array2 = [3, 4, 5, 6, 7]
common_values = find_common_values(array1, array2)
print("Common values:", common_values)