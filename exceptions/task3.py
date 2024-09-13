# Define a class with a method that raises an exception
class MyClass:
    def throw_exception(self):
        # Raise a custom exception
        raise Exception("This is an exception thrown from throw_exception method.")

# Main class (or just the main execution part of the program)
if __name__ == "__main__":
    obj = MyClass()
    # Call the method without a try block to handle the exception
    obj.throw_exception()
