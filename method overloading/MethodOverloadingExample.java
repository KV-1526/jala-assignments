public class MethodOverloadingExample {

    // Method 1: Takes an integer parameter
    public void display(int num) {
        System.out.println("Integer method called with value: " + num);
    }

    // Method 2: Takes a string parameter
    public void display(String text) {
        System.out.println("String method called with value: " + text);
    }

    public static void main(String[] args) {
        MethodOverloadingExample example = new MethodOverloadingExample();

        // Calling the methods with different parameter types
        example.display(10);       // Calls the integer version
        example.display("Hello");  // Calls the string version
    }
}
