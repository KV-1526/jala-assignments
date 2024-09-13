import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class WriteTextFileWithBufferedWriter {
    public static void main(String[] args) {
        String filePath = "path/to/your/file.txt"; // Update this with your file path
        String textToWrite = "Hello, World!\nJava is fun.\nWriting files is easy.";

        try (BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(filePath))) {
            // Write the text to the file
            bufferedWriter.write(textToWrite);
            
            // Optionally, you can use bufferedWriter.newLine() to add a new line if you are writing multiple lines
            bufferedWriter.newLine();
            bufferedWriter.write("This is an additional line.");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
