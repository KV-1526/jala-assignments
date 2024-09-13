def my_function(a, b=None):
    if b is not None:
        # Function called with two arguments
        print("a =", a, "b =", b)
    else:
        # Function called with one argument
        print("a =", a)

# Call the function with different numbers of arguments
my_function(10)
my_function(20, 30)