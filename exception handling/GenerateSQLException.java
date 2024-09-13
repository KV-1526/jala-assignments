import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class GenerateSQLException {
    public static void main(String[] args) {
        // Database URL with incorrect details
        String url = "jdbc:mysql://localhost:3306/non_existent_database";
        String username = "wrong_user";
        String password = "wrong_password";

        Connection connection = null;
        Statement statement = null;

        try {
            // Attempt to connect to a non-existent database or with wrong credentials
            connection = DriverManager.getConnection(url, username, password);
            statement = connection.createStatement();
            
            // Attempting to execute a query (this will not be reached due to connection failure)
            String query = "SELECT * FROM some_table";
            statement.executeQuery(query);
            
        } catch (SQLException e) {
            // Handling the SQLException
            System.out.println("Exception caught: SQL error occurred.");
            e.printStackTrace(); // Print stack trace for debugging
        } finally {
            // Close resources in the finally block
            try {
                if (statement != null) statement.close();
                if (connection != null) connection.close();
            } catch (SQLException e) {
                System.out.println("Exception caught while closing resources.");
                e.printStackTrace();
            }
        }

        // This line will be executed after handling the exception
        System.out.println("Program continues after handling the SQLException.");
    }
}
