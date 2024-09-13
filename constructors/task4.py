class Person:
    def __init__(self, name, age, city):
        """Constructor for the Person class.

        Args:
            name: The person's name.
            age: The person's age.
            city: The person's city.
        """

        # Attributes of the constructor
        self.name = name
        self.age = age
        self.city = city

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("City:", self.city)

# Create an object of the Person class
person1 = Person("gowtham", 21, "tirupati")

# Access and print the attributes of the object
person1.display_info()