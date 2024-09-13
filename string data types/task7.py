def sort_string(string):
  """Sorts a string in ascending order.

  Args:
    string: The string to sort.

  Returns:
    The sorted string.
  """

  # Convert the string to a list of characters
  char_list = list(string)

  # Sort the list of characters
  char_list.sort()

  # Convert the sorted list back to a string
  sorted_string = ''.join(char_list)

  return sorted_string

# Get user input
string = input("Enter a string: ")

# Sort the string and print the result
sorted_string = sort_string(string)
print("After sorting the string appears like:", sorted_string)