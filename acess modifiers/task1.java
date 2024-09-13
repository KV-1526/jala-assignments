// Base class with private fields and methods
class BaseClass {
    // Private fields
    private int privateField1 = 10;
    private String privateField2 = "Private Data";

    // Private method
    private void privateMethod() {
        System.out.println("Private method in BaseClass");
    }

    // Public method to access private fields and methods
    public void display() {
        System.out.println("PrivateField1: " + privateField1);
        System.out.println("PrivateField2: " + privateField2);
        privateMethod(); // Call private method
    }

    public static void main(String[] args) {
        // Create an instance of BaseClass
        BaseClass base = new BaseClass();
        
        // Access private fields and methods via a public method
        base.display();
    }
}



// Subclass extending BaseClass
class SubClass extends BaseClass {
    // Attempt to access private fields and methods from BaseClass
    void accessBaseClassMembers() {
        // Cannot access private fields or methods from BaseClass
        // Uncommenting the following lines will result in compilation errors
        // System.out.println("PrivateField1: " + privateField1);
        // System.out.println("PrivateField2: " + privateField2);
        // privateMethod(); 

        System.out.println("Cannot access private fields or methods from BaseClass");
    }

    public static void main(String[] args) {
        // Create an instance of SubClass
        SubClass sub = new SubClass();
        
        // Attempt to access private members
        sub.accessBaseClassMembers();
        
        // Access BaseClass public method
        sub.display(); // Will print private fields and call private method through public method
    }
}
