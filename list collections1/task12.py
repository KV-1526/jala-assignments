# Creating a string list
string_list = ["Alice", "Bob", "Kishore", "Diana", "Eve"]

# Checking if 'Kishore' is in the list using index method
try:
    index = string_list.index('Kishore')
    print("'Kishore' is present in the list at index:", index)
except ValueError:
    print("'Kishore' is not present in the list.")
