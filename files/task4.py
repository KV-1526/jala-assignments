import os

def read_file_stream_random_access(file_path, offset, length):
  """Reads a file stream using random access.

  Args:
    file_path: The path to the file.
    offset: The starting offset in bytes.
    length: The number of bytes to read.

  Returns:
    The bytes read from the file.
  """

  try:
    with open(file_path, 'rb') as file:
      file.seek(offset, os.SEEK_SET)  # Set the file pointer to the specified offset
      data = file.read(length)
      return data
  except FileNotFoundError:
    print(f"File not found: {file_path}")
    return None

# Example usage:
file_path ="example.txt"
offset = 10
length = 20

data = read_file_stream_random_access(file_path, offset, length)

if data:
  print(data.decode('utf-8'))  # Decode the bytes to a string
else:
  print("Failed to read the file.")