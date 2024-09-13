class ExampleClass:
    
    # Constructor (Instance variable)
    def __init__(self, value):
        self.value = value  # Instance variable

    # Instance method (can access instance variables)
    def instance_method(self):
        return f"The value in the instance is: {self.value}"
    
    # Static method (doesn't access instance variables)
    @staticmethod
    def static_method():
        return "This is a static method, and it cannot access instance variables."

# Creating an instance of ExampleClass
example = ExampleClass(42)

# Calling the instance method
print(example.instance_method())  # Output: The value in the instance is: 42

# Calling the static method (can be called using both the instance and class)
print(ExampleClass.static_method())  # Output: This is a static method, and it cannot access instance variables.
print(example.static_method())       # Output: This is a static method, and it cannot access instance variables.
