# Define a method that raises an exception with a custom message
def validate_age(age):
    if age < 18:
        raise Exception(f"Invalid age: {age}. You must be at least 18 years old.")
    else:
        print("Age is valid.")

# Main execution
if __name__ == "__main__":
    user_age = 15  # Set an age value that will cause the exception
    # Call the function, which will throw the exception
    validate_age(user_age)
