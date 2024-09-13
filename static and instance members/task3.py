class Car:
    # Static variable (class variable)
    num_wheels = 4  # Shared by all cars
    
    # Constructor (Instance variables)
    def __init__(self, make, model):
        self.make = make        # Instance variable (specific to the object)
        self.model = model      # Instance variable (specific to the object)
    
    # Method to display car details
    def display_details(self):
        print(f"Car make: {self.make}")
        print(f"Car model: {self.model}")
        print(f"Number of wheels (static variable): {Car.num_wheels}")

# Creating an instance (this will invoke the instance constructor)
my_car = Car("Toyota", "Corolla")

# Accessing the instance method to display details
my_car.display_details()
