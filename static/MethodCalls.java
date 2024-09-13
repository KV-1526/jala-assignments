public class MethodCalls {
    private static int staticVariable = 10;
    private int instanceVariable = 20;

    public static void staticMethod() {
        System.out.println("Static method called");
    }

    public void instanceMethod() {
        System.out.println("Instance method called");
    }

    public static void main(String[] args) {
        // Calling static method directly
        staticMethod();

        // Creating an instance to call instance method
        MethodCalls obj = new MethodCalls();
        obj.instanceMethod();

        // Accessing static variable directly
        System.out.println("Static variable: " + staticVariable);

        // Accessing instance variable through the instance
        System.out.println("Instance variable: " + obj.instanceVariable);
    }
}