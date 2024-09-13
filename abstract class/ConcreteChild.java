// Abstract class with abstract methods
abstract class AbstractBase {
    // Abstract method (does not have a body)
    abstract void abstractMethod();

    // Non-abstract method (has a body)
    void nonAbstractMethod() {
        System.out.println("This is a non-abstract method in the abstract class.");
    }
}

// Concrete class extending the abstract class
public class ConcreteChild extends AbstractBase {
    // Implement the abstract method
    @Override
    void abstractMethod() {
        System.out.println("Implementation of the abstract method in ConcreteChild.");
    }

    // Main method to demonstrate the creation of an instance within the child class
    public static void main(String[] args) {
        // Create an instance of ConcreteChild
        ConcreteChild childInstance = new ConcreteChild();

        // Call the abstract method
        childInstance.abstractMethod();

        // Call the non-abstract method
        childInstance.nonAbstractMethod();

        // Create an instance of ConcreteChild within itself
        ConcreteChild innerInstance = new ConcreteChild();
        
        // Call the abstract method through the inner instance
        innerInstance.abstractMethod();
    }
}
