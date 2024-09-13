class MyClass:
    def __init__(self):
        self.existing_field = "I exist!"

def access_field(obj, field_name):
    # This function attempts to access an attribute of the object
    try:
        value = getattr(obj, field_name)
        print(f"Value of '{field_name}': {value}")
    except AttributeError:
        print(f"Caught an exception: The field '{field_name}' does not exist.")

# Main execution
if __name__ == "__main__":
    obj = MyClass()

    # Attempt to access an existing field
    print("Attempting to access existing field:")
    access_field(obj, 'existing_field')

    # Attempt to access a non-existing field
    print("\nAttempting to access non-existing field:")
    access_field(obj, 'non_existing_field')
