public class PrintVariables {
    private static int staticVariable = 10;
    private int instanceVariable = 20;

    public static void main(String[] args) {
        // Accessing static variable directly
        System.out.println("Static variable: " + staticVariable);

        // Creating an instance to access instance variable
        PrintVariables obj = new PrintVariables();
        System.out.println("Instance variable: " + obj.instanceVariable);
    }
}