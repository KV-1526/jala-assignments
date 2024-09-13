class MyClass:
    public_field1 = 10
    public_field2 = 20

    def public_method1(self):
        print("This is a public method")

    def public_method2(self):
        print("Accessing public fields:", self.public_field1, self.public_field2)


class OtherClass:
    def __init__(self):
        self.my_object = MyClass()

    def access_public_members(self):
        print("Accessing public members from another class:")
        print(self.my_object.public_field1)
        self.my_object.public_method1()


if __name__ == "__main__":
    obj = MyClass()
    obj.public_method1()
    print(obj.public_field2)

    other_obj = OtherClass()
    other_obj.access_public_members()