import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.BufferedWriter;

public class WriteTextToFile {
    public static void main(String[] args) {
        // Path to the .txt file
        String filePath = "output.txt"; // Replace with the path where you want to create the file

        // Text to be written to the file
        String text = "Hello, World!\nThis is a sample text file written using OutputStream.";

        try (FileOutputStream fileOutputStream = new FileOutputStream(filePath);
             OutputStreamWriter outputStreamWriter = new OutputStreamWriter(fileOutputStream);
             BufferedWriter bufferedWriter = new BufferedWriter(outputStreamWriter)) {

            // Write text to the file
            bufferedWriter.write(text);
            bufferedWriter.newLine(); // Optional: Adds a new line after the text

        } catch (IOException e) {
            // Handling the exception
            System.out.println("Exception caught: Error writing to the file.");
            e.printStackTrace(); // Print stack trace for debugging
        }

        System.out.println("Text has been written to the file successfully.");
    }
}
