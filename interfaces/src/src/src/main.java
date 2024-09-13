package src;

public class Main {
    public static void main(String[] args) {
        MyClass obj = new MyClass();
        obj.parentMethod();  // Calls the method from ParentInterface
        obj.childMethod();   // Calls the method from ChildInterface
    }
}
