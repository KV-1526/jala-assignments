class MyClass:
  # Static variable
  static_var = 10

  def __init__(self):
    pass

  def change_static_var(self):
    MyClass.static_var = 20

# Accessing the static variable before modification
print("Static variable before modification:", MyClass.static_var)

# Directly changing the static variable within the class
MyClass.static_var = 30

# Accessing the static variable after modification
print("Static variable after modification:", MyClass.static_var)

# Creating an object and accessing the static variable
obj = MyClass()
print("Static variable through object:", obj.static_var)