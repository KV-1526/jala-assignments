import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;

public class ReadTextFileWithFileReader {
    public static void main(String[] args) {
        String filePath = "path/to/your/file.txt"; // Update this with your file path

        try (
            FileReader fileReader = new FileReader(filePath);
            BufferedReader bufferedReader = new BufferedReader(fileReader)
        ) {
            String line;
            while ((line = bufferedReader.readLine()) != null) {
                System.out.println(line);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
