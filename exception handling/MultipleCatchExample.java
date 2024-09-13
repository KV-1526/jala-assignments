public class MultipleCatchExample {
    public static void main(String[] args) {
        try {
            int[] numbers = {1, 2, 3};
            int result = numbers[3];  // This will cause ArrayIndexOutOfBoundsException

            int division = 10 / 0;    // This will cause ArithmeticException
            System.out.println("Result: " + division);

        } catch (ArrayIndexOutOfBoundsException e) {
            // This block handles the ArrayIndexOutOfBoundsException
            System.out.println("Exception caught: Array index is out of bounds.");

        } catch (ArithmeticException e) {
            // This block handles the ArithmeticException
            System.out.println("Exception caught: Cannot divide by zero.");

        } catch (Exception e) {
            // This block catches any other exceptions that aren't caught above
            System.out.println("Exception caught: An unexpected error occurred.");
        }

        // This line will be executed after handling exceptions
        System.out.println("Program continues after handling the exceptions.");
    }
}
