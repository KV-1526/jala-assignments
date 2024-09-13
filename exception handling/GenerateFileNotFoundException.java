import java.io.FileInputStream;
import java.io.FileNotFoundException;

public class GenerateFileNotFoundException {
    public static void main(String[] args) {
        FileInputStream fileInputStream = null;
        
        try {
            // Attempting to open a file that does not exist
            fileInputStream = new FileInputStream("non_existent_file.txt");
            System.out.println("File opened successfully.");
        } catch (FileNotFoundException e) {
            // Handling the exception
            System.out.println("Exception caught: File not found.");
            e.printStackTrace(); // Print stack trace for debugging
        } finally {
            // Closing the file input stream if it was opened
            if (fileInputStream != null) {
                try {
                    fileInputStream.close();
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        }
        
        // This line will be executed after handling the exception
        System.out.println("Program continues after handling the FileNotFoundException.");
    }
}
