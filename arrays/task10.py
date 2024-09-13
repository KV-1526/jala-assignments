def find_duplicates(array):
  """Finds duplicate values in an array.

  Args:
    array: The array to search.

  Returns:
    A list of duplicate values.
  """

  duplicates = []
  seen = set()

  for num in array:
    if num in seen:
      duplicates.append(num)
    else:
      seen.add(num)

  return duplicates

# Example usage:
numbers = [1, 2, 3, 4, 5, 2, 3, 6]
duplicate_values = find_duplicates(numbers)
print("Duplicate values:", duplicate_values)