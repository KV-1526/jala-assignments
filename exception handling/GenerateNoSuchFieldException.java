import java.lang.reflect.Field;

public class GenerateNoSuchFieldException {
    public static void main(String[] args) {
        try {
            // Attempt to access a non-existent field in the SampleClass
            Class<?> clazz = SampleClass.class;
            Field field = clazz.getField("nonExistentField"); // This will cause NoSuchFieldException

            // If the field is found, this line will execute
            System.out.println("Field found: " + field.getName());
        } catch (NoSuchFieldException e) {
            // Handling the exception
            System.out.println("Exception caught: Field not found.");
            e.printStackTrace(); // Print stack trace for debugging
        }

        // This line will be executed after handling the exception
        System.out.println("Program continues after handling the NoSuchFieldException.");
    }
}

// A simple class with no fields
class SampleClass {
    // This class has no fields
}
