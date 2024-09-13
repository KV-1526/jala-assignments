public class IncrementDecrement {

    // Method to demonstrate increment and decrement operators
    public static void incrementDecrementDemo() {
        int num = 10;

        // Pre-increment: First increment, then use the value
        System.out.println("Pre-increment: " + (++num));  // Output: 11

        // Post-increment: First use the value, then increment
        System.out.println("Post-increment: " + (num++));  // Output: 11
        System.out.println("Value after post-increment: " + num);  // Output: 12

        // Pre-decrement: First decrement, then use the value
        System.out.println("Pre-decrement: " + (--num));  // Output: 11

        // Post-decrement: First use the value, then decrement
        System.out.println("Post-decrement: " + (num--));  // Output: 11
        System.out.println("Value after post-decrement: " + num);  // Output: 10
    }

    public static void main(String[] args) {
        // Call the method to demonstrate increment and decrement
        incrementDecrementDemo();
    }
}
