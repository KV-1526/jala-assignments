public class StringEqualsExample {
    public static void main(String[] args) {
        // Define two strings
        String str1 = "Hello, World!";
        String str2 = "Hello, World!";
        String str3 = "hello, world!";
        
        // Compare strings using equals()
        boolean isEqual1 = str1.equals(str2); // true
        boolean isEqual2 = str1.equals(str3); // false

        // Print the results
        System.out.println("str1 equals str2: " + isEqual1);
        System.out.println("str1 equals str3: " + isEqual2);
    }
}
