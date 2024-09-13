public class MyClass {
    private int instanceVariable;

    public MyClass(int instanceVariable) {
        this.instanceVariable = instanceVariable;
    }

    public static void printInstanceVariable(MyClass object) {
        System.out.println(object.instanceVariable);
    }

    public static void main(String[] args) {
        MyClass obj = new MyClass(10);
        printInstanceVariable(obj); // Output: 10
    }
}