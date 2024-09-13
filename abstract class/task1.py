from abc import ABC, abstractmethod

# Abstract class
class AbstractClassExample(ABC):
    def __init__(self, value):
        self.value = value

    # Abstract method (must be implemented by any subclass)
    @abstractmethod
    def abstract_method(self):
        pass

    # Non-abstract method (can be used as-is or overridden by subclasses)
    def non_abstract_method(self):
        return f"Non-abstract method: value is {self.value}"

# Concrete subclass that implements the abstract method
class ConcreteClass(AbstractClassExample):
    def abstract_method(self):
        return f"Abstract method implemented: value is {self.value}"

# Another concrete subclass
class AnotherConcreteClass(AbstractClassExample):
    def abstract_method(self):
        return f"Different implementation of abstract method: value is {self.value * 2}"

# Usage
if __name__ == "__main__":
    # Creating an object of the concrete class
    obj1 = ConcreteClass(10)
    print(obj1.abstract_method())      # Calls the implemented abstract method
    print(obj1.non_abstract_method())  # Calls the non-abstract method from the abstract class

    obj2 = AnotherConcreteClass(5)
    print(obj2.abstract_method())      # Calls the implemented abstract method in another subclass
    print(obj2.non_abstract_method())  # Calls the inherited non-abstract method
