def find_second_largest(array):
  """Finds the second largest number in an array.

  Args:
    array: The array to search.

  Returns:
    The second largest number, or None if the array has fewer than two elements.
  """

  if len(array) < 2:
    return None

  largest = second_largest = array[0]

  for num in array:
    if num > largest:
      second_largest = largest
      largest = num
    elif num > second_largest and num != largest:
      second_largest = num

  return second_largest

# Example usage:
numbers = [1, 2, 3, 4, 5, 100, -10]
second_largest_num = find_second_largest(numbers)
print("Second largest number:", second_largest_num)