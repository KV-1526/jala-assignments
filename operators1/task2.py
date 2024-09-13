# Function to demonstrate the working of unary operators
def unary_operations(a, res):
    print(f"Initial values: a = {a}, res = {res}")
    
    # a++: Post-increment (In Python, simulate by returning a, then increment)
    res = a
    a += 1
    print(f"After a++: a = {a}, res = {res}")
    
    # a--: Post-decrement (Simulate by returning a, then decrement)
    res = a
    a -= 1
    print(f"After a--: a = {a}, res = {res}")
    
    # ++a: Pre-increment (Increment first, then return)
    a += 1
    res = a
    print(f"After ++a: a = {a}, res = {res}")
    
    # --a: Pre-decrement (Decrement first, then return)
    a -= 1
    res = a
    print(f"After --a: a = {a}, res = {res}")

# Input from user
a = int(input("Enter a value for a: "))
res = int(input("Enter a value for res: "))

# Call the function
unary_operations(a, res)
