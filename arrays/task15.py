def count_even_odd(array):
  """Counts the number of even and odd numbers in an array.

  Args:
    array: The array to analyze.

  Returns:
    A tuple containing the count of even and odd numbers.
  """

  even_count = 0
  odd_count = 0

  for num in array:
    if num % 2 == 0:
      even_count += 1
    else:
      odd_count += 1

  return even_count, odd_count

# Example usage:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_count, odd_count = count_even_odd(numbers)
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)