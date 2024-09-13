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
    def abstract_method(self):
        return f"Abstract method implemented: value is {self.value}"

    def access_non_abstract_methods(self):
        # Accessing the non-abstract method of the abstract class
        return self.non_abstract_method()

# Main block
if __name__ == "__main__":
    # Creating an object of the subclass
    obj = ConcreteClass(20)
    
    # Accessing the non-abstract method from the abstract class
    print(obj.access_non_abstract_methods())  # Accessing via a method in the child class
