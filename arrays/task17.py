def contains_elements(array, element1, element2):
  """Checks if an array contains two specified elements.

  Args:
    array: The array to search.
    element1: The first element to search for.
    element2: The second element to search for.

  Returns:
    True if the array contains both elements, False otherwise.
  """

  return element1 in array and element2 in array

# Example usage:
numbers = [1, 2, 3, 4, 5, 12, 23]
if contains_elements(numbers, 12, 23):
  print("Array contains both elements.")
else:
  print("Array does not contain both elements.")