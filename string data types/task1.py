def reverse_string(string):
  """Reverses a string without using the built-in reverse function.

  Args:
    string: The string to reverse.

  Returns:
    The reversed string.
  """

  reversed_string = ""
  for char in string:
    reversed_string = char + reversed_string
  return reversed_string

# Get user input
string = input("Enter a string: ")

# Reverse the string and print the result
reversed_string = reverse_string(string)
print("Reversed string:", reversed_string)