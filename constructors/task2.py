class Superclass:
    def __init__(self, value=None):
        self.value = value
        print(f"Superclass constructor called with value: {self.value}")

class Subclass(Superclass):
    def __init__(self, value=None, extra_value=None):
        # Call the default constructor of Superclass
        super().__init__(value)
        # Additional initialization in the subclass
        self.extra_value = extra_value
        print(f"Subclass constructor called with extra_value: {self.extra_value}")

# Create an instance of Subclass
obj = Subclass(10, 20)
