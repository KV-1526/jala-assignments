# Global variable
global_var = "I am a global variable"

def my_function():
    # Local variable with the same name as the global variable
    local_var = "I am a local variable"

    # Accessing both variables within the function
    print("Inside the function:")
    print("Global variable:", global_var)
    print("Local variable:", local_var)

# Calling the function
my_function()

# Accessing the global variable outside the function
print("\nOutside the function:")
print("Global variable:", global_var)