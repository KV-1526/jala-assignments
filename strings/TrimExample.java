public class TrimExample {
    public static void main(String[] args) {
        // Define a string with leading and trailing whitespace
        String str = "   Hello, World!   ";
        
        // Trim the string
        String trimmedStr = str.trim();
        
        // Print the original and trimmed strings
        System.out.println("Original string: [" + str + "]");
        System.out.println("Trimmed string: [" + trimmedStr + "]");
    }
}
