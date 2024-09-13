public class SubstringExample {
    public static void main(String[] args) {
        // Define a string
        String myString = "Hello, World!";

        // Extract a substring from index 7 to the end
        String substring1 = myString.substring(7);
        System.out.println("Substring from index 7: " + substring1);

        // Extract a substring from index 0 to 5 (end index is exclusive)
        String substring2 = myString.substring(0, 5);
        System.out.println("Substring from index 0 to 5: " + substring2);

        // Extract a substring from index 7 to 12
        String substring3 = myString.substring(7, 12);
        System.out.println("Substring from index 7 to 12: " + substring3);
    }
}
