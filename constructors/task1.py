class MyClass:
    def __init__(self, arg1=None, arg2=None):
        print("Default constructor called")
        if arg1 is not None:
            print("One argument constructor called with arg1:", arg1)
        if arg2 is not None:
            print("Two argument constructor called with arg1:", arg1, "and arg2:", arg2)

class Main:
    def main(self):
        # Calling the default constructor
        obj1 = MyClass()

        # Calling the one argument constructor
        obj2 = MyClass(10)

        # Calling the two argument constructor
        obj3 = MyClass(20, 30)

if __name__ == "__main__":
    Main().main()