public class GenerateNullPointerException {
    public static void main(String[] args) {
        // Create a reference variable without initializing it
        String text = null;

        try {
            // Attempt to call a method on a null object reference
            int length = text.length(); // This will cause NullPointerException
            System.out.println("Length of the string: " + length);
        } catch (NullPointerException e) {
            // Handling the exception
            System.out.println("Exception caught: Null pointer exception occurred.");
            e.printStackTrace(); // Print stack trace for debugging
        }

        // This line will be executed after handling the exception
        System.out.println("Program continues after handling the NullPointerException.");
    }
}
