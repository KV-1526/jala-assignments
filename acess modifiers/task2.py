class BaseClass:
    def __init__(self, x):
        self._x = x  # Protected attribute

    def _process_value(self):
        """
        Protected method to process and return the value of _x.
        """
        return self._x * 2

class DerivedClass(BaseClass):
    def display_value(self):
        """
        Method to display the processed value using the protected method from BaseClass.
        """
        processed_value = self._process_value()  # Accessing protected method
        print(f"Processed value: {processed_value}")

# Input: Creating an instance of DerivedClass
value = int(input("Enter value of x: "))
derived = DerivedClass(x=value)

# Output: Displaying the processed value
derived.display_value()
