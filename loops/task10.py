def is_palindrome(s):
  """Checks if a string is a palindrome.

  Args:
    s: The string to check.

  Returns:
    True if the string is a palindrome, False otherwise.
  """

  s = s.lower()  # Convert to lowercase to ignore case
  return s == s[::-1]  # Reverse the string and compare

# Example usage:
word = "racecar"
if is_palindrome(word):
  print(f"{word} is a palindrome.")
else:
  print(f"{word} is not a palindrome.")