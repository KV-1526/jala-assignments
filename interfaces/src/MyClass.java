// Class implementing both interfaces
public class MyClass implements FirstInterface, SecondInterface {

    // Implement method from FirstInterface
    @Override
    public void methodFromFirst() {
        System.out.println("Implementation of methodFromFirst() from FirstInterface.");
    }

    // Implement method from SecondInterface
    @Override
    public void methodFromSecond() {
        System.out.println("Implementation of methodFromSecond() from SecondInterface.");
    }

    // Main method to demonstrate calling the implemented methods
    public static void main(String[] args) {
        // Create an instance of MyClass
        MyClass myClassInstance = new MyClass();
        
        // Call methods implemented from both interfaces
        myClassInstance.methodFromFirst();
        myClassInstance.methodFromSecond();
    }
}
