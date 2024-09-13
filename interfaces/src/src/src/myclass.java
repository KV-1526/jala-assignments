package src.src.src;

public class MyClass implements ChildInterface {
    @Override
    public void parentMethod() {
        System.out.println("Implementation of parentMethod.");
    }

    @Override
    public void childMethod() {
        System.out.println("Implementation of childMethod.");
    }
}
