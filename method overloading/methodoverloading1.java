public class MethodOverloading1 {

    public static void printMessage(String message) {
        System.out.println("String message: " + message);
    }

    public static void printMessage(int number) {
        System.out.println("Integer number: " + number);
    }

    public static void main(String[] args) {
        String message = "Hello, world!";
        int number = 42;

        // Calling the method with a string parameter
        printMessage(message);

        // Calling the method with an integer parameter
        printMessage(number);
    }
}