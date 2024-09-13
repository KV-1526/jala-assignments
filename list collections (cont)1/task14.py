# Creating a Python list with mixed data types
my_list = [1, "hello", 3.14, True, [5, 6]]

# 1. Dynamic Size
print("Original list:", my_list)
my_list.append("new item")  # Adding an element
print("List after adding an item:", my_list)

# 2. Indexing
print("Element at index 1:", my_list[1])  # Accessing element at index 1

# 3. Mixed Data Types
print("List contains mixed data types:")
for item in my_list:
    print(f"Item: {item}, Type: {type(item)}")
