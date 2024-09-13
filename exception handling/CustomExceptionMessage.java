public class CustomExceptionMessage {

    // Method that throws an exception with a custom message
    public static void validateNumber(int number) {
        if (number < 0) {
            // Throwing an exception with a custom message
            throw new IllegalArgumentException("Invalid number: Number cannot be negative.");
        }
        System.out.println("Valid number: " + number);
    }

    public static void main(String[] args) {
        // Calling the method with a negative number to trigger the exception
        validateNumber(-5);

        // This line will not execute due to the exception thrown above
        System.out.println("This line will not be printed.");
    }
}
