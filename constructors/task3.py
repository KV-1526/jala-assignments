class PublicConstructor:
    def __init__(self, value):
        self.value = value
        print(f"Public constructor called with value: {self.value}")

# Usage
obj = PublicConstructor(10)


class ProtectedConstructor:
    def __init__(self, value):
        self._value = value
        print(f"Protected constructor called with value: {self._value}")

class Subclass(ProtectedConstructor):
    def __init__(self, value):
        super().__init__(value)
        print(f"Subclass constructor called with value: {self._value}")

# Usage
obj = Subclass(20)


class PrivateConstructor:
    def __init__(self, value):
        self.__value = value
        print(f"Private constructor called with value: {self.__value}")

    def get_value(self):
        return self.__value

# Usage
obj = PrivateConstructor(30)
print(obj.get_value())
# Trying to access obj.__value directly will raise an AttributeError
# print(obj.__value)  # This will cause an error


class DefaultConstructor:
    def __init__(self, value=0):
        self.value = value
        print(f"Default constructor called with value: {self.value}")

# Usage
obj1 = DefaultConstructor()   # Uses default value
obj2 = DefaultConstructor(40) # Uses provided value
