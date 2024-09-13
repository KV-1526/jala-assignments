class MyClass:
    def my_method(self, *args):
        if len(args) == 1 and isinstance(args[0], int):
            self.my_method_int(args[0])
        elif len(args) == 2 and isinstance(args[0], int) and isinstance(args[1], str):
            self.my_method_int_str(args[0], args[1])
        else:
            print("Invalid parameters")

    def my_method_int(self, param1):
        print(f"Method with one integer: {param1}")

    def my_method_int_str(self, param1, param2):
        print(f"Method with an integer and a string: {param1}, {param2}")

# Create an instance of MyClass
obj = MyClass()

# Call the method with an integer
obj.my_method(10)  # Output: Method with one integer: 10

# Call the method with an integer and a string
obj.my_method(10, "Hello")  # Output: Method with an integer and a string: 10, Hello

# Call the method with invalid parameters
obj.my_method(10, 20)  # Output: Invalid parameters
