def remove_duplicates(array):
  """Removes duplicate elements from an array.

  Args:
    array: The array to modify.

  Returns:
    The array with duplicate elements removed.
  """

  unique_elements = []
  seen = set()

  for element in array:
    if element not in seen:
      unique_elements.append(element)
      seen.add(element)

  return unique_elements

# Example usage:
numbers = [1, 2, 3, 4, 5, 2, 3, 6]
unique_numbers = remove_duplicates(numbers)
print(unique_numbers)