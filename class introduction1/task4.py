class Car:
    # Class variables (shared by all instances of the class)
    num_wheels = 4   # Class member
    has_engine = True # Class member
    vehicle_type = 'Car'  # Class member

    # Constructor (Instance variables)
    def __init__(self, make, model, color, maxSpeed):
        self.make = make        # Instance variable (field)
        self.model = model      # Instance variable (field)
        self.color = color      # Field: Color of the car
        self.maxSpeed = maxSpeed  # Field: Max speed of the car in km/h

    # Method to display car details
    def display_details(self):
        print(f"Car make: {self.make}")
        print(f"Car model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Max Speed: {self.maxSpeed} km/h")
        print(f"Number of wheels: {Car.num_wheels}")
        print(f"Has engine: {Car.has_engine}")
        print(f"Vehicle type: {Car.vehicle_type}")

# Creating an object of Car class with the name myObj
myObj = Car("Toyota", "Corolla", "Red", 180)

# Printing the values of the fields color and maxSpeed
print(f"Color of the car: {myObj.color}")
print(f"Max Speed of the car: {myObj.maxSpeed} km/h")
