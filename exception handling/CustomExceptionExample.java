// Custom Exception Class
class InvalidAgeException extends Exception {
    // Constructor with custom error message
    public InvalidAgeException(String message) {
        super(message);
    }
}

public class CustomExceptionExample {

    // Method that throws the custom exception
    public static void checkAge(int age) throws InvalidAgeException {
        if (age < 18) {
            // Throwing the custom exception with a message
            throw new InvalidAgeException("Age must be 18 or older.");
        }
        System.out.println("Age is valid: " + age);
    }

    public static void main(String[] args) {
        try {
            // Calling the method with an invalid age to trigger the exception
            checkAge(15);
        } catch (InvalidAgeException e) {
            // Handling the custom exception
            System.out.println("Exception caught: " + e.getMessage());
        }

        // Program continues after handling the exception
        System.out.println("Program continues after handling the custom exception.");
    }
}
