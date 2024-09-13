# Define a custom exception class
class InvalidAgeError(Exception):
    def __init__(self, age, message="Age must be at least 18."):
        self.age = age
        self.message = message
        super().__init__(self.message)

# Define a function to validate age using the custom exception
def validate_age(age):
    if age < 18:
        raise InvalidAgeError(age, f"Invalid age: {age}. You must be at least 18 years old.")
    else:
        print("Age is valid.")

# Main execution
if __name__ == "__main__":
    try:
        user_age = 15  # Set an invalid age to trigger the custom exception
        validate_age(user_age)
    except InvalidAgeError as e:
        print(f"Caught an exception: {e}")
