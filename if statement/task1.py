# Function to check whether a number is positive or negative
def check_number():
    # Input: Taking a number from the user
    num = float(input("Enter a number: "))
    
    # Check if the number is positive, negative or zero
    if num > 0:
        print(f"{num} is a positive number")
    elif num < 0:
        print(f"{num} is a negative number")
    else:
        print(f"{num} is neither positive nor negative")

# Call the function
check_number()
