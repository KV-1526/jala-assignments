class MyClass:
    def display(self, a, b=None):
        if b is None:
            print(f"Single parameter: {a}")
        else:
            print(f"Two parameters: {a}, {b}")

# Create an instance of MyClass
obj = MyClass()

# Call the method with one parameter
obj.display(10)  # Output: Single parameter: 10

# Call the method with two parameters
obj.display(10, 20)  # Output: Two parameters: 10, 20


class MyClass:
    def display(self, *args):
        if len(args) == 1:
            print(f"Single parameter: {args[0]}")
        elif len(args) == 2:
            print(f"Two parameters: {args[0]}, {args[1]}")
        else:
            print("Unsupported number of parameters")

# Create an instance of MyClass
obj = MyClass()

# Call the method with one parameter
obj.display(10)  # Output: Single parameter: 10

# Call the method with two parameters
obj.display(10, 20)  # Output: Two parameters: 10, 20

# Call the method with three parameters
obj.display(10, 20, 30)  # Output: Unsupported number of parameters
