// Superclass with multiple constructors
class SuperClass {
    // Default constructor
    public SuperClass() {
        System.out.println("Superclass default constructor called");
    }

    // Parameterized constructor with one argument
    public SuperClass(int arg1) {
        System.out.println("Superclass one-argument constructor called with value: " + arg1);
    }

    // Parameterized constructor with two arguments
    public SuperClass(int arg1, String arg2) {
        System.out.println("Superclass two-argument constructor called with values: " + arg1 + ", " + arg2);
    }
}

// Subclass that calls superclass constructors
class SubClass extends SuperClass {
    // Default constructor of subclass
    public SubClass() {
        // Calls the default constructor of the superclass
        super();
        System.out.println("Subclass default constructor called");
    }

    // Subclass constructor with one argument
    public SubClass(int arg1) {
        // Calls the one-argument constructor of the superclass
        super(arg1);
        System.out.println("Subclass one-argument constructor called with value: " + arg1);
    }

    // Subclass constructor with two arguments
    public SubClass(int arg1, String arg2) {
        // Calls the two-argument constructor of the superclass
        super(arg1, arg2);
        System.out.println("Subclass two-argument constructor called with values: " + arg1 + ", " + arg2);
    }
}

// Main class to test the constructors
public class mainainClass {
    public static void main(String[] args) {
        // Instantiate SubClass to call each constructor
        SubClass obj1 = new SubClass();             // Calls default constructors of both classes
        SubClass obj2 = new SubClass(10);           // Calls one-argument constructors of both classes
        SubClass obj3 = new SubClass(20, "Hello");  // Calls two-argument constructors of both classes
    }
}
