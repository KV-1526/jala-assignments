public class ArithmeticExceptionHandled {
    public static void main(String[] args) {
        int numerator = 10;
        int denominator = 0;

        try {
            // Attempt division, which may cause an ArithmeticException
            int result = numerator / denominator;
            System.out.println("Result: " + result);
        } catch (ArithmeticException e) {
            // This block handles the exception
            System.out.println("Exception caught: Cannot divide by zero.");
        }

        // This line will be executed even if an exception is thrown
        System.out.println("Program continues after handling the exception.");
    }
}
