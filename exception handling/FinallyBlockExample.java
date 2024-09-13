public class FinallyBlockExample {
    public static void main(String[] args) {
        try {
            // Code that may throw an exception
            int result = 10 / 0; // This will cause ArithmeticException
            System.out.println("Result: " + result);
        } catch (ArithmeticException e) {
            // Handling the exception
            System.out.println("Exception caught: Cannot divide by zero.");
        } finally {
            // This block will always execute
            System.out.println("Finally block executed.");
        }

        // Program continues after try-catch-finally
        System.out.println("Program continues after the try-catch-finally block.");
    }
}
