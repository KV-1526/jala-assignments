// Abstract class with non-abstract methods
abstract class AbstractClass {
    // Non-abstract method (has a body)
    void nonAbstractMethod() {
        System.out.println("This is a non-abstract method in the abstract class.");
    }

    // Abstract method (does not have a body)
    abstract void abstractMethod();
}

// Concrete class extending the abstract class
public class ConcreteClass extends AbstractClass {
    // Implement the abstract method
    @Override
    void abstractMethod() {
        System.out.println("Implementation of the abstract method in ConcreteClass.");
    }

    // Main method to demonstrate the creation of an instance within the child class
    public static void main(String[] args) {
        // Create an instance of ConcreteClass
        ConcreteClass outerInstance = new ConcreteClass();
        
        // Call the non-abstract method from the current instance
        outerInstance.nonAbstractMethod();

        // Create an instance of ConcreteClass within itself
        ConcreteClass innerInstance = new ConcreteClass();

        // Call the non-abstract method through the inner instance
        innerInstance.nonAbstractMethod();
    }
}
