// Interface with two methods
interface MyInterface {
    // Method declarations
    void methodOne();
    void methodTwo();
}

// Abstract class implementing the interface
abstract class AbstractClass implements MyInterface {
    // Provide implementation for one of the interface methods
    @Override
    public void methodOne() {
        System.out.println("Implementation of methodOne() in AbstractClass.");
    }

    // No implementation for methodTwo(), so the class remains abstract
}

// Concrete class extending the abstract class
public class ConcreteClass extends AbstractClass {
    // Provide implementation for the remaining interface method
    @Override
    public void methodTwo() {
        System.out.println("Implementation of methodTwo() in ConcreteClass.");
    }

    // Main method to demonstrate calling the implemented method
    public static void main(String[] args) {
        // Create an instance of ConcreteClass
        ConcreteClass concreteInstance = new ConcreteClass();
        
        // Call the method implemented in AbstractClass
        concreteInstance.methodOne();

        // Call the method implemented in ConcreteClass
        concreteInstance.methodTwo();
    }
}
