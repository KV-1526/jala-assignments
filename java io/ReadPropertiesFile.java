




import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;

public class ReadPropertiesFile {
    public static void main(String[] args) {
        String filePath = "path/to/your/config.properties"; // Update this with the path to your properties file

        // Create a Properties object
        Properties properties = new Properties();

        try (InputStream inputStream = new FileInputStream(filePath)) {
            // Load properties from the file
            properties.load(inputStream);

            // Read properties values
            String dbUrl = properties.getProperty("database.url");
            String dbUsername = properties.getProperty("database.username");
            String dbPassword = properties.getProperty("database.password");

            // Print properties values
            System.out.println("Database URL: " + dbUrl);
            System.out.println("Database Username: " + dbUsername);
            System.out.println("Database Password: " + dbPassword);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
