public class MethodOverloadingReturnType {

    // Method 1: Returns an integer
    public int calculate(int num) {
        System.out.println("Integer method called");
        return num * 2; // For example, multiply by 2
    }

    // Method 2: Returns a double
    public double calculate(double num) {
        System.out.println("Double method called");
        return num * 2.5; // For example, multiply by 2.5
    }

    public static void main(String[] args) {
        MethodOverloadingReturnType example = new MethodOverloadingReturnType();

        // Calling the methods with different types
        int result1 = example.calculate(5); // Calls the integer version
        double result2 = example.calculate(5.0); // Calls the double version

        System.out.println("Integer result: " + result1);
        System.out.println("Double result: " + result2);
    }
}
