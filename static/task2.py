class MyClass:
  # Static variable
  static_var = 10

  def __init__(self):
    pass

  def access_static_var(self):
    print("Static variable:", MyClass.static_var)

# Accessing the static variable through the class name
print("Static variable:", MyClass.static_var)

# Creating an object and accessing the static variable through the class name
obj = MyClass()
obj.access_static_var()