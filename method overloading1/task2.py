def my_function(a, b=None, c=None):
    if b is not None and c is not None:
        # Function called with three arguments
        print("a =", a, "b =", b, "c =", c)
    elif b is not None:
        # Function called with two arguments
        print("a =", a, "b =", b)
    else:
        # Function called with one argument
        print("a =", a)

# Call the function with different argument orders
my_function(10)
my_function(20, 30)
my_function(40, 50, 60)