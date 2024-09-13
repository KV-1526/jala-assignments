import os

def check_file_permissions(file_path):
  """Checks whether a file has read and write access permissions.

  Args:
    file_path: The path to the file.

  Returns:
    A tuple of (read_access, write_access), where each value is True or False.
  """

  try:
    with open(file_path, 'r') as file:
      file.read()  # Check read access
      file.write("test")  # Check write access
      return True, True
  except PermissionError:
    if "Permission denied" in str(e):
      # Check for specific permission denied message
      if "read" in str(e):
        return False, True  # Read permission denied, write permission granted
      elif "write" in str(e):
        return True, False  # Read permission granted, write permission denied
      else:
        return False, False  # Both read and write permissions denied
    else:
      raise e  # Re-raise other exceptions

# Example usage:
file_path = "example.txt"
read_access, write_access = check_file_permissions(file_path)

if read_access and write_access:
  print("File has both read and write access.")
elif read_access:
  print("File has read access only.")
elif write_access:
  print("File has write access only.")
else:
  print("File has no access permissions.")