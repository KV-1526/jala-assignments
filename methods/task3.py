class Calculator:
    def calculate_sum_and_product(self, a, b):
        """Calculates the sum and product of two numbers.

        Args:
          a: The first number.
          b: The second number.

        Returns:
          A tuple containing the sum and product.
        """

        sum = a + b
        product = a * b
        return sum, product

# Create a Calculator object
calculator = Calculator()

# Get user input
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

# Calculate the sum and product
sum, product = calculator.calculate_sum_and_product(a, b)

# Print the results
print("sum =", sum, "and product =", product)