# Creating a list with different data types (heterogeneous)
my_list = [1, "hello", 3.14, [2, 3], True]

# Accessing elements by index (indexable)
print(my_list[1])  # Output: hello
print(my_list[-1]) # Output: True

# Modifying elements (mutable)
my_list[2] = 3.14159
print(my_list)  # Output: [1, 'hello', 3.14159, [2, 3], True]

# Adding elements (dynamic size)
my_list.append("new element")
print(my_list)  # Output: [1, 'hello', 3.14159, [2, 3], True, 'new element']

# Removing elements (dynamic size)
my_list.remove("hello")
print(my_list)  # Output: [1, 3.14159, [2, 3], True, 'new element']
