public class SplitExample {
    public static void main(String[] args) {
        // Define a string
        String str = "apple,banana,orange,grape";
        
        // Split the string by comma
        String[] fruits = str.split(",");
        
        // Print each fruit
        System.out.println("Fruits:");
        for (String fruit : fruits) {
            System.out.println(fruit);
        }
    }
}


public class SplitWithLimitExample {
    public static void main(String[] args) {
        // Define a string
        String str = "apple,banana,orange,grape";
        
        // Split the string by comma with a limit
        String[] fruits = str.split(",", 3);
        
        // Print each fruit
        System.out.println("Fruits with limit:");
        for (String fruit : fruits) {
            System.out.println(fruit);
        }
    }
}

