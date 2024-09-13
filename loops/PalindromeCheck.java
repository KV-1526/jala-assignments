public class PalindromeCheck {
    public static void main(String[] args) {
        String originalString = "racecar"; // Replace with the string you want to check

        // Reverse the string
        String reversedString = new StringBuilder(originalString).reverse().toString();

        // Check if the original and reversed strings are equal
        if (originalString.equalsIgnoreCase(reversedString)) {
            System.out.println(originalString + " is a palindrome.");
        } else {
            System.out.println(originalString + " is not a palindrome.");
        }
    }
}