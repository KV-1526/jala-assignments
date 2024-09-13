class MyClass:
    def __init__(self, a, b=0):
        self.a = a
        self.b = b

    def display(self):
        print("a =", self.a)
        print("b =", self.b)

# Create objects with different arguments
obj1 = MyClass(10)  # Using only the required argument
obj2 = MyClass(20, 30)  # Using both arguments

# Display the values
obj1.display()
obj2.display()