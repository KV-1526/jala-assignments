// Abstract class with abstract and non-abstract methods
abstract class AbstractAnimal {
    // Abstract method (does not have a body)
    abstract void makeSound();

    // Non-abstract method (has a body)
    void sleep() {
        System.out.println("This animal is sleeping.");
    }

    // Non-abstract method (has a body)
    void eat() {
        System.out.println("This animal is eating.");
    }
}

// Concrete class extending the abstract class
public class Dog extends AbstractAnimal {
    // Providing implementation for the abstract method
    @Override
    void makeSound() {
        System.out.println("The dog barks.");
    }

    // Optionally override non-abstract methods if needed
    @Override
    void eat() {
        System.out.println("The dog is eating kibble.");
    }

    // Main method to demonstrate usage
    public static void main(String[] args) {
        // Create an instance of Dog
        Dog myDog = new Dog();
        
        // Call methods
        myDog.makeSound(); // Calls the overridden abstract method
        myDog.sleep();     // Calls the non-abstract method from AbstractAnimal
        myDog.eat();       // Calls the overridden non-abstract method
    }
}

