public class ArithmeticOperations {

    // Function to add two numbers
    public static int add(int a, int b) {
        return a + b;
    }

    // Function to subtract two numbers
    public static int subtract(int a, int b) {
        return a - b;
    }

    // Function to multiply two numbers
    public static int multiply(int a, int b) {
        return a * b;
    }

    // Function to divide two numbers
    public static double divide(double a, double b) {
        if (b != 0) {
            return a / b;
        } else {
            System.out.println("Division by zero is not allowed.");
            return 0; // Handle division by zero safely
        }
    }

    public static void main(String[] args) {
        // Variables for arithmetic operations
        int x = 20, y = 10;

        // Performing arithmetic operations
        System.out.println("Addition: " + add(x, y));          // Output: 30
        System.out.println("Subtraction: " + subtract(x, y));  // Output: 10
        System.out.println("Multiplication: " + multiply(x, y));  // Output: 200
        System.out.println("Division: " + divide(x, y));       // Output: 2.0
    }
}
