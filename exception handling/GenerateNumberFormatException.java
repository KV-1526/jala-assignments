public class GenerateNumberFormatException {
    public static void main(String[] args) {
        String invalidNumber = "abc123"; // This string is not a valid number

        try {
            // Attempt to convert an invalid number format to an integer
            int number = Integer.parseInt(invalidNumber); // This will cause NumberFormatException
            System.out.println("Converted number: " + number);
        } catch (NumberFormatException e) {
            // Handling the exception
            System.out.println("Exception caught: Number format exception occurred.");
            e.printStackTrace(); // Print stack trace for debugging
        }

        // This line will be executed after handling the exception
        System.out.println("Program continues after handling the NumberFormatException.");
    }
}
