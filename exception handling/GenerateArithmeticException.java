public class GenerateArithmeticException {
    public static void main(String[] args) {
        int numerator = 10;
        int denominator = 0; // This will cause an ArithmeticException

        // Division by zero, which will generate ArithmeticException
        int result = numerator / denominator;

        // This line will not be executed because the exception is thrown above
        System.out.println("Result: " + result);
    }
}
