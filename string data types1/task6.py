def find_max_occurring_char(string):
  """Finds the maximum occurring character in a string.

  Args:
    string: The string to analyze.

  Returns:
    A tuple containing the maximum occurring character and its frequency.
  """

  char_count = {}
  max_char = None
  max_count = 0

  for char in string:
    if char in char_count:
      char_count[char] += 1
    else:
      char_count[char] = 1

    if char_count[char] > max_count:
      max_char = char
      max_count = char_count[char]

  return max_char, max_count

# Get user input
string = input("Enter a string: ")

# Find the maximum occurring character and print the result
max_char, max_count = find_max_occurring_char(string)
print("The highest frequency of the character '{}' appears as {} times".format(max_char, max_count))