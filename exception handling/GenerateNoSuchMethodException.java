import java.lang.reflect.Method;

public class GenerateNoSuchMethodException {
    public static void main(String[] args) {
        try {
            // Attempt to access a non-existent method in the SampleClass
            Class<?> clazz = SampleClass.class;
            Method method = clazz.getMethod("nonExistentMethod"); // This will cause NoSuchMethodException

            // If the method is found, this line will execute
            System.out.println("Method found: " + method.getName());
        } catch (NoSuchMethodException e) {
            // Handling the exception
            System.out.println("Exception caught: Method not found.");
            e.printStackTrace(); // Print stack trace for debugging
        }

        // This line will be executed after handling the exception
        System.out.println("Program continues after handling the NoSuchMethodException.");
    }
}

// A simple class with a method
class SampleClass {
    public void existingMethod() {
        // A method that exists in the class
    }
}
