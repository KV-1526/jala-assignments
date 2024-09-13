class A:
    def __init__(self):
        self.a_instance_var = 10

    def method_a1(self):
        print("Method A1")

    def method_a2(self):
        print("Method A2")

    def overridden_method(self):
        print("Overridden method in A")


class B(A):
    def __init__(self):
        super().__init__()
        self.b_instance_var = 20

    def method_b1(self):
        print("Method B1")

    def method_b2(self):
        print("Method B2")

    def overridden_method(self):
        print("Overridden method in B")


class C(B):
    def __init__(self):
        super().__init__()
        self.c_instance_var = 30

    def method_c1(self):
        print("Method C1")

    def method_c2(self):
        print("Method C2")

    def overridden_method(self):
        print("Overridden method in C")


class Main:
    def main(self):
        a_obj = A()
        b_obj = B()
        c_obj = C()

        # Calling methods on A object
        a_obj.method_a1()
        a_obj.method_a2()
        a_obj.overridden_method()

        # Calling methods on B object
        b_obj.method_a1()  # Inherited from A
        b_obj.method_a2()  # Inherited from A
        b_obj.method_b1()
        b_obj.method_b2()
        b_obj.overridden_method()  # Overridden method in B

        # Calling methods on C object
        c_obj.method_a1()  # Inherited from A
        c_obj.method_a2()  # Inherited from A
        c_obj.method_b1()  # Inherited from B
        c_obj.method_b2()  # Inherited from B
        c_obj.method_c1()
        c_obj.method_c2()
        c_obj.overridden_method()  # Overridden method in C

        # Calling overridden method with super class reference
        a_ref = B()
        a_ref.overridden_method()  # Calls overridden method in B

        # Runtime polymorphism with data members
        print("A object's instance variable:", a_obj.a_instance_var)
        print("B object's instance variable:", b_obj.a_instance_var)  # Inherited from A
        print("C object's instance variable:", c_obj.a_instance_var)  # Inherited from A

if __name__ == "__main__":
    Main().main()