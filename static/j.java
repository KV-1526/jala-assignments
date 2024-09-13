public class MyClass {
    private static int staticVariable = 10;

    public void instanceMethod() {
        System.out.println(staticVariable); // Accessing static variable
        staticMethod(); // Calling static method
    }

    public static void staticMethod() {
        System.out.println("Static method called");
    }

    public static void main(String[] args) {
        MyClass obj = new MyClass();
        obj.instanceMethod();
    }
}