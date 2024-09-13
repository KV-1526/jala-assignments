class Car:
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
        print()

# Creating multiple objects of Car class
car1 = Car("Toyota", "Corolla", "Red", 180)
car2 = Car("Honda", "Civic", "Blue", 200)
car3 = Car("Ford", "Mustang", "Black", 250)

# Calling the display_details() method for each object
car1.display_details()
car2.display_details()
car3.display_details()
