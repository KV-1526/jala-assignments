public class IndexOfExample {
    public static void main(String[] args) {
        // Define a string
        String myString = "Hello, World!";

        // Find the index of a character
        int indexChar = myString.indexOf('W');
        System.out.println("Index of 'W': " + indexChar);

        // Find the index of a substring
        int indexSubstring = myString.indexOf("World");
        System.out.println("Index of \"World\": " + indexSubstring);

        // Find the index of a character starting from a specific index
        int indexCharFrom = myString.indexOf('o', 5);
        System.out.println("Index of 'o' after index 5: " + indexCharFrom);

        // Find the index of a substring starting from a specific index
        int indexSubstringFrom = myString.indexOf("o", 5);
        System.out.println("Index of \"o\" after index 5: " + indexSubstringFrom);

        // Find the index of a substring not present in the string
        int indexNotFound = myString.indexOf("Java");
        System.out.println("Index of \"Java\": " + indexNotFound);
    }
}
