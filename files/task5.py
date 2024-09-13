def read_file_stream_to_index(file_path, index):
  """Reads a file stream up to a specified index.

  Args:
    file_path: The path to the file.
    index: The index to read up to (0-based).

  Returns:
    The contents of the file up to the specified index.
  """

  try:
    with open(file_path, 'rb') as file:
      file.seek(0, os.SEEK_SET)  # Set the file pointer to the beginning
      data = file.read(index + 1)  # Read up to the specified index (inclusive)
      return data.decode('utf-8')  # Decode the bytes to a string
  except FileNotFoundError:
    print(f"File not found: {file_path}")
    return None

# Example usage:
file_path = "example.txt"
index_to_read = 100

data = read_file_stream_to_index(file_path, index_to_read)

if data:
  print(data)
else:
  print("Failed to read the file.")