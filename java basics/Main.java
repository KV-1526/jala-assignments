class VariableScopeExample {
    // Global variable (instance variable)
    int num = 100;

    public void display() {
        // Local variable with the same name as the global variable
        int num = 50;

        // Printing the local variable (this will shadow the global variable)
        System.out.println("Local variable 'num': " + num);

        // Printing the global variable using 'this' keyword
        System.out.println("Global variable 'num': " + this.num);
    }
}

public class Main {
    public static void main(String[] args) {
        // Create an object of the class
        VariableScopeExample example = new VariableScopeExample();

        // Call the method to display both local and global variables
        example.display();
    }
}

