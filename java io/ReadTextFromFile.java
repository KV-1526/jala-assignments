import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.io.IOException;

public class ReadTextFromFile {
    public static void main(String[] args) {
        // Path to the .txt file
        String filePath = "Hello, World!\r\n" + //
                        "This is a sample text file.\r\n" + //
                        ""; // Replace with the path to your .txt file

        try (FileInputStream fileInputStream = new FileInputStream(filePath);
             InputStreamReader inputStreamReader = new InputStreamReader(fileInputStream);
             BufferedReader bufferedReader = new BufferedReader(inputStreamReader)) {

            String line;
            // Read the file line by line
            while ((line = bufferedReader.readLine()) != null) {
                System.out.println(line);
            }

        } catch (IOException e) {
            // Handling the exception
            System.out.println("Exception caught: Error reading the file.");
            e.printStackTrace(); // Print stack trace for debugging
        }
    }
}
