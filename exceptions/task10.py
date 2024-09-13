def instantiate_class(class_name):
    # This function attempts to instantiate a class by its name
    try:
        # Dynamically retrieve the class from globals() using its name
        cls = globals()[class_name]
        instance = cls()
        return instance
    except KeyError:
        # KeyError will be raised if the class_name is not found in globals()
        raise NameError(f"Class '{class_name}' not found.")

# Define a known class for demonstration
class KnownClass:
    def __init__(self):
        print("KnownClass instance created.")

# Main execution
if __name__ == "__main__":
    try:
        # Attempt to instantiate a class that does not exist
        class_name = 'NonExistentClass'
        print(f"Attempting to instantiate class: {class_name}")
        instance = instantiate_class(class_name)
    except NameError as e:
        print(f"Caught an exception: {e}")
