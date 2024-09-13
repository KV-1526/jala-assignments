public class MethodOverloading {

    public static void printNumbers(int num1, int num2) {
        System.out.println("Integer numbers: " + num1 + " and " + num2);
    }

    public static void printNumbers(double num1, double num2) {
        System.out.println("Double numbers: " + num1 + " and " + num2);
    }

    public static void main(String[] args) {
        int num1 = 10;
        int num2 = 20;
        double num3 = 3.14;
        double num4 = 2.718;

        // Calling the method with integer parameters
        printNumbers(num1, num2);

        // Calling the method with double parameters
        printNumbers(num3, num4);
    }
}