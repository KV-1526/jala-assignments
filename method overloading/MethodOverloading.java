public class MethodOverloading {

    public static void printNumbers(int num) {
        System.out.println("One number: " + num);
    }

    public static void printNumbers(int num1, int num2) {
        System.out.println("Two numbers: " + num1 + " and " + num2);
    }

    public static void main(String[] args) {
        int num1 = 10;
        int num2 = 20;

        // Calling the method with one parameter
        printNumbers(num1);

        // Calling the method with two parameters
        printNumbers(num1, num2);
    }
}