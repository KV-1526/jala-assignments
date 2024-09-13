from package1.public_class import PublicClass

# This class is in the same package as PublicClass
class SamePackageClass:
    def access_public_members(self):
        obj = PublicClass()
        print(obj.public_field)       # Accessing public field
        print(obj.public_method())    # Accessing public method
