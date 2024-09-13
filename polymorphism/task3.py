class MathOperations:
    
    def add(self, *args):
        """
        Method to add numbers. This simulates method overloading.
        It handles different numbers of arguments.
        """
        if len(args) == 2:
            # Handle the case of two arguments
            a, b = args
            result = a + b
            print(f"Sum of two numbers: {a} + {b} = {result}")
        elif len(args) == 3:
            # Handle the case of three arguments
            a, b, c = args
            result = a + b + c
            print(f"Sum of three numbers: {a} + {b} + {c} = {result}")
        else:
            print("Unsupported number of arguments")

# Creating an instance of MathOperations
math_op = MathOperations()

# Calling the 'add' method with two arguments
math_op.add(10, 20)  # Outputs: Sum of two numbers: 10 + 20 = 30

# Calling the 'add' method with three arguments
math_op.add(10, 20, 30)  # Outputs: Sum of three numbers: 10 + 20 + 30 = 60

# Calling the 'add' method with a different number of arguments
math_op.add(10)  # Outputs: Unsupported number of arguments
