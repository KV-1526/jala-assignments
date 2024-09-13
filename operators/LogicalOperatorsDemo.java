public class LogicalOperatorsDemo {

    public static void main(String[] args) {
        // Variables for demonstration
        boolean a = true;
        boolean b = false;

        // Logical AND (&&)
        if (a && b) {
            System.out.println("Both a and b are true.");
        } else {
            System.out.println("Logical AND (a && b) is false because both conditions are not true.");
        }

        // Logical OR (||)
        if (a || b) {
            System.out.println("Logical OR (a || b) is true because at least one condition is true.");
        } else {
            System.out.println("Both conditions are false.");
        }

        // Logical NOT (!)
        System.out.println("Logical NOT (!a): " + !a);  // Will print false because a is true
        System.out.println("Logical NOT (!b): " + !b);  // Will print true because b is false
    }
}

