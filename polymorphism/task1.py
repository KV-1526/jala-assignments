class Calculator:
    
    # Method to handle two or three parameters using default arguments
    def add(self, a, b, c=None):
        if c is not None:
            # If three arguments are provided, add all three
            result = a + b + c
            print(f"Sum of three numbers: {a} + {b} + {c} = {result}")
        else:
            # If only two arguments are provided, add the two
            result = a + b
            print(f"Sum of two numbers: {a} + {b} = {result}")

# Create an instance of the Calculator class
calc = Calculator()

# Calling the 'add' method with two arguments
calc.add(10, 20)  # This will invoke the logic for two parameters

# Calling the 'add' method with three arguments
calc.add(10, 20, 30)  # This will invoke the logic for three parameters
