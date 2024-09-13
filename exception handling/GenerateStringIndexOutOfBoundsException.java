public class GenerateStringIndexOutOfBoundsException {
    public static void main(String[] args) {
        String text = "Hello, world!"; // A sample string

        try {
            // Attempt to access an index that is out of bounds
            char character = text.charAt(20); // Index 20 is out of bounds for the string length
            System.out.println("Character at index 20: " + character);
        } catch (StringIndexOutOfBoundsException e) {
            // Handling the exception
            System.out.println("Exception caught: String index out of bounds.");
            e.printStackTrace(); // Print stack trace for debugging
        }

        // This line will be executed after handling the exception
        System.out.println("Program continues after handling the StringIndexOutOfBoundsException.");
    }
}
