public class ExampleClass {

    // Static variables
    private static int staticVar1 = 10;
    private static int staticVar2 = 20;

    // Instance variables
    private int instanceVar1;
    private int instanceVar2;

    // Static method 1
    public static void staticMethod1() {
        System.out.println("Static Method 1");
        System.out.println("Static Variable 1: " + staticVar1);
        System.out.println("Static Variable 2: " + staticVar2);
    }

    // Static method 2
    public static void staticMethod2() {
        System.out.println("Static Method 2");
        // Accessing static variables
        System.out.println("Static Variable 1: " + staticVar1);
        System.out.println("Static Variable 2: " + staticVar2);
    }

    // Instance method 1
    public void instanceMethod1() {
        System.out.println("Instance Method 1");
        System.out.println("Instance Variable 1: " + instanceVar1);
        System.out.println("Instance Variable 2: " + instanceVar2);
    }

    // Instance method 2
    public void instanceMethod2() {
        System.out.println("Instance Method 2");
        System.out.println("Instance Variable 1: " + instanceVar1);
        System.out.println("Instance Variable 2: " + instanceVar2);
    }

    // Constructor
    public ExampleClass(int instanceVar1, int instanceVar2) {
        this.instanceVar1 = instanceVar1;
        this.instanceVar2 = instanceVar2;
    }

    // Main method
    public static void main(String[] args) {
        // Calling static methods
        ExampleClass.staticMethod1();
        ExampleClass.staticMethod2();

        // Creating an instance of the class
        ExampleClass example = new ExampleClass(100, 200);

        // Calling instance methods
        example.instanceMethod1();
        example.instanceMethod2();
    }
}
