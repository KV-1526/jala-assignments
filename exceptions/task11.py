def open_file(file_path):
    # This function attempts to open a file
    with open(file_path, 'r') as file:
        content = file.read()
        return content

# Main execution
if __name__ == "__main__":
    try:
        # Path to a file that is not accessible or does not exist
        file_path = '/root/protected_file.txt'  # This path is just an example
        print(f"Attempting to open the file: {file_path}")
        file_content = open_file(file_path)
        print(f"File content: {file_content}")
    except IOError as e:
        print(f"Caught an IOError: {e}")
