import io

def write_text_to_file(file_path, text):
  """Writes text to a .txt file using an InputStream.

  Args:
    file_path: The path to the .txt file.
    text: The text to write to the file.
  """

  with open(file_path, 'wb') as file:
    stream = io.StringIO(text)
    file.write(stream.read().encode('utf-8'))

# Example usage
file_path = "example.txt"
text_to_write = "This is the text to write to the file."

write_text_to_file(file_path, text_to_write)
print("Text written to", file_path)