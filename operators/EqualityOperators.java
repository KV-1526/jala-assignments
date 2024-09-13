public class EqualityOperators {

    // Method to demonstrate equal (==) and not equal (!=) operators
    public static void equalityCheck(int a, int b) {
        // Equal operator (==)
        if (a == b) {
            System.out.println(a + " is equal to " + b);
        } else {
            System.out.println(a + " is not equal to " + b);
        }

        // Not equal operator (!=)
        if (a != b) {
            System.out.println(a + " is not equal to " + b);
        } else {
            System.out.println(a + " is equal to " + b);
        }
    }

    public static void main(String[] args) {
        // Test values
        int x = 10;
        int y = 20;

        // Call the method to check equality and non-equality
        equalityCheck(x, y);

        // Another test case where values are equal
        int z = 10;
        equalityCheck(x, z);
    }
}
