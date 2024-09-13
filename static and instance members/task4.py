class Car:
    # Static variable (class variable)
    num_wheels = 4  # All cars have 4 wheels initially

    # Constructor (Instance variables)
    def __init__(self, make, model):
        self.make = make    # Instance variable
        self.model = model  # Instance variable

    # Instance method to display car details
    def display_details(self):
        print(f"Car make: {self.make}")
        print(f"Car model: {self.model}")
        print(f"Number of wheels (static variable): {Car.num_wheels}")

    # Class method to change the static variable
    @classmethod
    def change_num_wheels(cls, new_wheels):
        cls.num_wheels = new_wheels  # Changing the static variable

# Creating instances of the Car class
car1 = Car("Toyota", "Corolla")
car2 = Car("benz", "Civic")

# Displaying details before changing the static variable
print("Before changing the static variable:")
car1.display_details()
car2.display_details()

# Changing the static variable using the class method
Car.change_num_wheels(6)

# Displaying details after changing the static variable
print("\nAfter changing the static variable:")
car1.display_details()
car2.display_details()
