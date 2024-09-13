import java.io.BufferedOutputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.charset.StandardCharsets;

public class WriteTextFile {
    public static void main(String[] args) {
        String filePath = "path/to/your/file.txt"; // Update this with your file path
        String textToWrite = "Hello, World!\nJava is fun.\nWriting files is easy.";

        try (
            FileOutputStream fileOutputStream = new FileOutputStream(filePath);
            BufferedOutputStream bufferedOutputStream = new BufferedOutputStream(fileOutputStream)
        ) {
            // Convert the text to bytes using UTF-8 encoding
            byte[] textBytes = textToWrite.getBytes(StandardCharsets.UTF_8);
            
            // Write the bytes to the file
            bufferedOutputStream.write(textBytes);
            
            // Optionally, flush and close the stream
            bufferedOutputStream.flush();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
