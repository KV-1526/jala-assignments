public class StringEqualsIgnoreCaseExample {
    public static void main(String[] args) {
        String str1 = "Hello, World!";
        String str2 = "HELLO, WORLD!";
        String str3 = "Hello, World!";
        
        boolean isEqual1 = str1.equalsIgnoreCase(str2); // true
        boolean isEqual2 = str1.equalsIgnoreCase(str3); // true

        System.out.println("str1 equalsIgnoreCase str2: " + isEqual1);
        System.out.println("str1 equalsIgnoreCase str3: " + isEqual2);
    }
}

public class StringStartsWithExample {
    public static void main(String[] args) {
        String str = "Hello, World!";
        
        boolean startsWithHello = str.startsWith("Hello"); // true
        boolean startsWithWorld = str.startsWith("World", 7); // true

        System.out.println("str starts with 'Hello': " + startsWithHello);
        System.out.println("str starts with 'World' from index 7: " + startsWithWorld);
    }
}
public class StringEndsWithExample {
    public static void main(String[] args) {
        String str = "Hello, World!";
        
        boolean endsWithWorld = str.endsWith("World!"); // true
        boolean endsWithHello = str.endsWith("Hello"); // false

        System.out.println("str ends with 'World!': " + endsWithWorld);
        System.out.println("str ends with 'Hello': " + endsWithHello);
    }
}

public class StringCompareToExample {
    public static void main(String[] args) {
        String str1 = "apple";
        String str2 = "banana";
        String str3 = "apple";
        
        int comparison1 = str1.compareTo(str2); // negative value
        int comparison2 = str1.compareTo(str3); // 0
        int comparison3 = str2.compareTo(str1); // positive value

        System.out.println("str1 compared to str2: " + comparison1);
        System.out.println("str1 compared to str3: " + comparison2);
        System.out.println("str2 compared to str1: " + comparison3);
    }
}
