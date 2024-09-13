import java.io.FileWriter;
import java.io.IOException;

public class WriteTextFileWithFileWriter {
    public static void main(String[] args) {
        String filePath = "path/to/your/file.txt"; // Update this with your file path
        String textToWrite = "Hello, World!\nJava is fun.\nWriting files is easy.";

        try (FileWriter fileWriter = new FileWriter(filePath)) {
            // Write the text to the file
            fileWriter.write(textToWrite);
            
            // Optionally, you can also use fileWriter.append(textToWrite) to append text instead of overwriting
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
