def reverse_array(array):
  """Reverses an array of integer values.

  Args:
    array: The array to reverse.

  Returns:
    The reversed array.
  """

  return array[::-1]

# Example usage:
numbers = [1, 2, 3, 4, 5]
reversed_numbers = reverse_array(numbers)
print(reversed_numbers)