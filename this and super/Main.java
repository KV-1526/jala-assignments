class MyClass {
    // Instance variables
    int id;
    String name;

    // Constructor to initialize the instance variables
    MyClass(int id, String name) {
        this.id = id;       // 'this' keyword is used to refer to the current object's 'id'
        this.name = name;   // 'this' keyword is used to refer to the current object's 'name'
    }

    // Method to print instance members
    void printDetails() {
        // Using 'this' to refer to the instance variables
        System.out.println("ID: " + this.id);
        System.out.println("Name: " + this.name);
    }
}
public class Main {
    public static void main(String[] args) {
        // Create an object of MyClass and initialize it
        MyClass obj = new MyClass(101, "John Doe");

        // Call the method to print details
        obj.printDetails();  // This will print the instance members using 'this'
    }
}
