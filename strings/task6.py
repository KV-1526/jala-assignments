import re

def match_string_against_regex(string, regex):
  """Matches a string against a regular expression.

  Args:
    string: The string to match.
    regex: The regular expression pattern.

  Returns:
    True if the string matches the regular expression, False otherwise.
  """

  match = re.match(regex, string)
  return bool(match)

# Example usage
string_to_match = "The quick brown fox jumps over the lazy dog"
regex_pattern = r"quick brown fox"

if match_string_against_regex(string_to_match, regex_pattern):
  print("The string matches the regular expression.")
else:
  print("The string does not match the regular expression.")