class OverloadedMethods:
    
    def process(self, a, b=None):
        """
        Method to demonstrate function overloading based on parameter types.
        It handles:
        - Two integers
        - An integer and a string
        """
        if isinstance(a, int) and isinstance(b, int):
            # Handle the case where both parameters are integers
            result = a + b
            print(f"Sum of two integers: {a} + {b} = {result}")
        elif isinstance(a, int) and isinstance(b, str):
            # Handle the case where first parameter is an integer and second is a string
            result = str(a) + b
            print(f"Concatenation of integer and string: {a} + '{b}' = '{result}'")
        else:
            print("Unsupported parameter types")

# Creating an instance of OverloadedMethods
methods = OverloadedMethods()

# Calling the 'process' method with two integers
methods.process(10, 20)  # Outputs: Sum of two integers: 10 + 20 = 30

# Calling the 'process' method with an integer and a string
methods.process(10, " apples")  # Outputs: Concatenation of integer and string: 10 + ' apples' = '10 apples'

# Calling the 'process' method with unsupported parameter types
methods.process("hello", 10)  # Outputs: Unsupported parameter types
