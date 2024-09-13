// Interface with a single method
interface MyInterface {
    // Abstract method (does not have a body)
    void singleMethod();
}

// Class implementing the interface
public class MyClass implements MyInterface {
    // Provide implementation for the interface method
    @Override
    public void singleMethod() {
        System.out.println("Implementation of the singleMethod() in MyClass.");
    }

    // Main method to demonstrate calling the implemented method
    public static void main(String[] args) {
        // Create an instance of MyClass
        MyClass myClassInstance = new MyClass();

        // Call the method implemented from MyInterface
        myClassInstance.singleMethod();
    }
}
