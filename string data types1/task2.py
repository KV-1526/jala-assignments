def find_string_length(string):
  """Finds the length of a string without using a library function.

  Args:
    string: The string to find the length of.

  Returns:
    The length of the string.
  """

  length = 0
  for char in string:
    length += 1
  return length

# Get user input
string = input("Enter a string: ")

# Find the length of the string and print the result
length = find_string_length(string)
print("Length of the string:", length)