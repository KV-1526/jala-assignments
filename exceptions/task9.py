def read_file(file_path):
    # This function attempts to open and read a file
    with open(file_path, 'r') as file:
        content = file.read()
        return content

# Main execution
if __name__ == "__main__":
    try:
        # Path to a file that does not exist
        file_path = 'non_existent_file.txt'
        print(f"Attempting to read the file: {file_path}")
        file_content = read_file(file_path)
        print(f"File content: {file_content}")
    except FileNotFoundError:
        print(f"Caught an exception: The file '{file_path}' was not found.")
