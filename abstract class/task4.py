from abc import ABC, abstractmethod

# Abstract class
class AbstractClassExample(ABC):
    def __init__(self, value):
        self.value = value

    # Abstract method (must be implemented by subclass)
    @abstractmethod
    def abstract_method(self):
        pass

    # Non-abstract method
    def non_abstract_method(self):
        return f"Non-abstract method: value is {self.value}"

# Subclass implementing the abstract method
class ConcreteClass(AbstractClassExample):
    def __init__(self, value):
        super().__init__(value)  # Call the constructor of the parent class

    # Implementation of the abstract method
    def abstract_method(self):
        return f"Abstract method called: value is {self.value}"

    def create_instance_and_call_non_abstract_methods(self):
        # Creating an instance of the child class inside the child class
        obj = ConcreteClass(30)

        # Calling the non-abstract method from the abstract class
        print(obj.non_abstract_method())

# Main block
if __name__ == "__main__":
    # Create an instance of the child class and call the non-abstract method
    concrete_instance = ConcreteClass(50)
    concrete_instance.create_instance_and_call_non_abstract_methods()
