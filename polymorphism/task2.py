# Base class
class Animal:
    def sound(self):
        print("This animal makes a sound.")

# Derived class (Dog) overriding the sound method
class Dog(Animal):
    def sound(self):
        print("The dog barks.")

# Derived class (Cat) overriding the sound method
class Cat(Animal):
    def sound(self):
        print("The cat meows.")

# Derived class (Cow) overriding the sound method
class Cow(Animal):
    def sound(self):
        print("The cow moos.")

# Function that demonstrates runtime polymorphism
def animal_sound(animal):
    animal.sound()  # The actual method invoked depends on the object type

# Creating objects of each subclass
dog = Dog()
cat = Cat()
cow = Cow()

# Calling the animal_sound function with different animal objects
animal_sound(dog)  # Outputs: The dog barks.
animal_sound(cat)  # Outputs: The cat meows.
animal_sound(cow)  # Outputs: The cow moos.
