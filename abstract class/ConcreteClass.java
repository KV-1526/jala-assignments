// Abstract class with abstract and non-abstract methods
abstract class AbstractClass {
    // Abstract method (does not have a body)
    abstract void abstractMethod();

    // Non-abstract method (has a body)
    void nonAbstractMethod() {
        System.out.println("This is a non-abstract method in the abstract class.");
    }
}

// Concrete class extending the abstract class
public class ConcreteClass extends AbstractClass {
    // Provide implementation for the abstract method
    @Override
    void abstractMethod() {
        System.out.println("Implementation of the abstract method.");
    }

    // Main method to demonstrate usage
    public static void main(String[] args) {
        // Create an instance of ConcreteClass
        ConcreteClass concreteObj = new ConcreteClass();

        // Access the non-abstract method inherited from AbstractClass
        concreteObj.nonAbstractMethod();

        // Call the abstract method implemented in ConcreteClass
        concreteObj.abstractMethod();
    }
}
