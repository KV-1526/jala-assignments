class MyClass:
    def __init__(self, value):
        self.__value = value  # Private attribute

    def __private_method(self):
        """
        Private method to return the private value.
        """
        return f"Private value: {self.__value}"

    def public_method(self):
        """
        Public method to access the private method and attribute.
        """
        print(self.__private_method())

# Creating an instance of MyClass
obj = MyClass(10)

# Accessing the public method to demonstrate the use of private members
obj.public_method()

# Attempting to access private members directly (will raise AttributeError)
try:
    print(obj.__value)
except AttributeError as e:
    print(f"Error: {e}")

try:
    print(obj.__private_method())
except AttributeError as e:
    print(f"Error: {e}")

# Accessing private attribute via name mangling
print(obj._MyClass__value)  # This is technically possible but not recommended
