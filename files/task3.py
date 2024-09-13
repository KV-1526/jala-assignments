def read_file_stream(file_path):
  """Reads a file stream and returns its contents as a string.

  Args:
    file_path: The path to the file.

  Returns:
    The contents of the file as a string.
  """

  try:
    with open(file_path, 'r') as file:
      contents = file.read()
      return contents
  except FileNotFoundError:
    print(f"File not found: {file_path}")
    return None

# Example usage:
file_path = "example.txt"
contents = read_file_stream(file_path)

if contents:
  print(contents)
else:
  print("Failed to read the file.")