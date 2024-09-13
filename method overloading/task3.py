class MyClass:
    # First method definition
    def my_method(self, param1):
        print(f"First method called with: {param1}")

    # Second method definition (will override the first one)
    def my_method(self, param1):
        print(f"Second method called with: {param1}")

# Create an instance of MyClass
obj = MyClass()

# Call the method
obj.my_method(10)  # Output: Second method called with: 10
