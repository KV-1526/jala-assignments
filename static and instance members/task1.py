class Car:
    # Static (class) variable
    num_wheels = 4  # All cars have 4 wheels

    def __init__(self, make, model):
        self.make = make    # Instance variable
        self.model = model  # Instance variable

    # Instance method to display car details
    def display_details(self):
        print(f"Car make: {self.make}")
        print(f"Car model: {self.model}")
        # Accessing static variable using the class name
        print(f"Number of wheels: {Car.num_wheels}")

# Creating an instance of Car class
my_car = Car("Toyota", "Corolla")

# Accessing the static variable through the class name
print(f"Accessing static variable directly: Car.num_wheels = {Car.num_wheels}")

# Accessing the static variable through the instance
print(f"Accessing static variable through instance: my_car.num_wheels = {my_car.num_wheels}")

# Displaying car details including the static variable
my_car.display_details()
