# Main file to run the classes
from package1.same_package_class import SamePackageClass
from package2.different_package_class import DifferentPackageClass

# Accessing public members from the same package
print("Accessing public members from the same package:")
same_package_obj = SamePackageClass()
same_package_obj.access_public_members()

# Accessing public members from a different package
print("\nAccessing public members from a different package:")
different_package_obj = DifferentPackageClass()
different_package_obj.access_public_members()
