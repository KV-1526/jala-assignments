class Car:
    # Class variables (shared by all instances of the class)
    num_wheels = 4   # Class member
    has_engine = True # Class member
    vehicle_type = 'Car'  # Class member

    # Constructor (Instance variables)
    def __init__(self, make, model):
        self.make = make    # Field 1 (instance variable)
        self.model = model  # Field 2 (instance variable)

    # Method to display car details
    def display_details(self):
        print(f"Car make: {self.make}")
        print(f"Car model: {self.model}")
        print(f"Number of wheels: {Car.num_wheels}")
        print(f"Has engine: {Car.has_engine}")
        print(f"Vehicle type: {Car.vehicle_type}")

# Creating an instance of Car class
my_car = Car("Toyota", "Corolla")

# Calling the method to display car details
my_car.display_details()
