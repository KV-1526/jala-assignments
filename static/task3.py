class MyClass:
  # Static variable
  static_var = 10

  def __init__(self):
    pass

  def change_static_var(self):
    MyClass.static_var = 20

# Accessing the static variable before modification
print("Static variable before modification:", MyClass.static_var)

# Creating an object and calling the method to change the static variable
obj = MyClass()
obj.change_static_var()

# Accessing the static variable after modification
print("Static variable after modification:", MyClass.static_var)