public class ValueOfIntExample {
    public static void main(String[] args) {
        // Define an integer
        int number = 123;
        
        // Convert int to String
        String str = String.valueOf(number);
        
        // Print the result
        System.out.println("String representation of int: " + str);
    }
}

    }
}
public class ValueOfLongExample {
    public static void main(String[] args) {
        long number = 123456789L;
        String str = String.valueOf(number);
        System.out.println("String representation of long: " + str);
    }
}
public class ValueOfFloatExample {
    public static void main(String[] args) {
        float number = 12.34f;
        String str = String.valueOf(number);
        System.out.println("String representation of float: " + str);
    }
}
public class ValueOfDoubleExample {
    public static void main(String[] args) {
        double number = 123.456;
        String str = String.valueOf(number);
        System.out.println("String representation of double: " + str);
    }
}
public class ValueOfCharExample {
    public static void main(String[] args) {
        char character = 'A';
        String str = String.valueOf(character);
        System.out.println("String representation of char: " + str);
    }
}public class ValueOfObjectExample {
    public static void main(String[] args) {
        Object obj = new Object();
        String str = String.valueOf(obj);
        System.out.println("String representation of Object: " + str);

        // Example with null
        Object nullObj = null;
        String nullStr = String.valueOf(nullObj);
        System.out.println("String representation of null Object: " + nullStr);
    }
}

