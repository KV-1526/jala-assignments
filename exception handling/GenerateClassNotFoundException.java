public class GenerateClassNotFoundException {
    public static void main(String[] args) {
        try {
            // Attempting to load a class that does not exist
            Class<?> clazz = Class.forName("com.example.NonExistentClass");
            System.out.println("Class found: " + clazz.getName());
        } catch (ClassNotFoundException e) {
            // Handling the exception
            System.out.println("Exception caught: Class not found.");
            e.printStackTrace(); // Print stack trace for debugging
        }
        
        // This line will be executed after handling the exception
        System.out.println("Program continues after handling the ClassNotFoundException.");
    }
}
