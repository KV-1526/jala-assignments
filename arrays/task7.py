def insert_element(array, element, position):
  """Inserts an element at a specific position in an array.

  Args:
    array: The array to modify.
    element: The element to insert.
    position: The position to insert the element (0-based index).

  Returns:
    The modified array.
  """

  if position < 0 or position > len(array):
    raise IndexError("Invalid position")

  array.insert(position, element)
  return array

# Example usage:
numbers = [1, 2, 3, 4, 5]
inserted_array = insert_element(numbers, 100, 2)
print(inserted_array)