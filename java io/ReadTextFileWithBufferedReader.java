import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class ReadTextFileWithBufferedReader {
    public static void main(String[] args) {
        String filePath = "path/to/your/file.txt"; // Update this with your file path

        try (BufferedReader bufferedReader = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = bufferedReader.readLine()) != null) {
                System.out.println(line);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
