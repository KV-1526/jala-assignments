public class ArithmeticExceptionExample {

    public static void main(String[] args) {
        int dividend = 10;
        int divisor = 0;

        // Attempting to divide by zero
        int result = dividend / divisor;

        System.out.println("Result: " + result);
    }
}