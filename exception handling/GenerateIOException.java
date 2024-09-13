import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class GenerateIOException {
    public static void main(String[] args) {
        BufferedReader reader = null;

        try {
            // Attempting to open a file that we cannot read from, such as a directory
            reader = new BufferedReader(new FileReader("path_to_a_directory")); // This will cause IOException
            String line = reader.readLine(); // Attempt to read a line from the file
            System.out.println("Read line: " + line);
        } catch (IOException e) {
            // Handling the exception
            System.out.println("Exception caught: An I/O error occurred.");
            e.printStackTrace(); // Print stack trace for debugging
        } finally {
            // Closing the BufferedReader if it was opened
            if (reader != null) {
                try {
                    reader.close();
                } catch (IOException e) {
                    System.out.println("Exception caught while closing the BufferedReader.");
                    e.printStackTrace();
                }
            }
        }
        
        // This line will be executed after handling the exception
        System.out.println("Program continues after handling the IOException.");
    }
}
