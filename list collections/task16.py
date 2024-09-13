# Creating a list with some initial elements
my_list = ["Alice", "Bob", "Kishore", "Diana", "Eve"]

# Removing the element at index 3
del my_list[3]

# Printing the list to verify the element has been removed
print(my_list)

# Creating a list with some initial elements
my_list = ["Alice", "Bob", "Kishore", "Diana", "Eve"]

# Removing the element at index 3 and returning it
removed_element = my_list.pop(3)

# Printing the list to verify the element has been removed
print("Updated list:", my_list)

# Printing the removed element
print("Removed element:", removed_element)
