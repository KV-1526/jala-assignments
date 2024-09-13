public class MyClass {
    private int instanceVariable;

    public MyClass(int instanceVariable) {
        this.instanceVariable = instanceVariable;
    }

    public void instanceMethod() {
        System.out.println("Instance method called");
    }

    public static void staticMethod() {
        MyClass obj = new MyClass(10);
        obj.instanceMethod();
    }

    public static void main(String[] args) {
        staticMethod();
    }
}