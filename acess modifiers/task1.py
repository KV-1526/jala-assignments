class MyClass:
    def __init__(self):
        self.__private_field1 = 10
        self.__private_field2 = 20

    def __private_method(self):
        print("This is a private method")

    def public_method(self):
        print("Public field 1:", self.__private_field1)
        print("Public field 2:", self.__private_field2)
        self.__private_method()

class SubClass(MyClass):
    pass

if __name__ == "__main__":
    obj = MyClass()
    obj.public_method()

    # Trying to access private fields and methods from subclass (will raise AttributeError)
    try:
        sub_obj = SubClass()
        print(sub_obj.__private_field1)  # Raises AttributeError
        sub_obj.__private_method()  # Raises AttributeError
    except AttributeError as e:
        print(e)