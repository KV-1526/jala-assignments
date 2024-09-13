// Class with multiple constructors
class MyClass {
    // Default constructor
    public MyClass() {
        System.out.println("Default constructor called");
    }

    // One-argument constructor
    public MyClass(int arg1) {
        System.out.println("One-argument constructor called with value: " + arg1);
    }

    // Two-argument constructor
    public MyClass(int arg1, String arg2) {
        System.out.println("Two-argument constructor called with values: " + arg1 + ", " + arg2);
    }
}

// Main class to test the constructors
public class MainClass {
    public static void main(String[] args) {
        // Calling default constructor
        MyClass obj1 = new MyClass();

        // Calling one-argument constructor
        MyClass obj2 = new MyClass(10);

        // Calling two-argument constructor
        MyClass obj3 = new MyClass(20, "Hello");
    }
}
