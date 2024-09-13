package src;

public interface MyInterface {
    default void show() {
        System.out.println("This is the default implementation of the show method.");
    }
}
