class Car:
    # Static (class) variable
    num_wheels = 4

    def __init__(self, make, model):
        self.make = make    # Instance variable
        self.model = model  # Instance variable

    # Static method
    @staticmethod
    def show_vehicle_type():
        print("This is a car.")

    # Instance method
    def display_details(self):
        print(f"Car make: {self.make}")
        print(f"Car model: {self.model}")
        print(f"Number of wheels: {Car.num_wheels}")

# Creating an instance of the Car class
my_car = Car("Toyota", "Corolla")

# Accessing the static method through the instance
my_car.show_vehicle_type()  # Output: This is a car.

# Accessing the static method through the class name
Car.show_vehicle_type()  # Output: This is a car.

# Calling an instance method
my_car.display_details()
