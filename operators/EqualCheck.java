import java.util.Scanner;

public class EqualCheck {

    public static void main(String[] args) {
        // Create a Scanner object to read input from the user
        Scanner scanner = new Scanner(System.in);

        // Prompt the user to enter two numbers
        System.out.print("Enter the first number: ");
        int num1 = scanner.nextInt();

        System.out.print("Enter the second number: ");
        int num2 = scanner.nextInt();

        // Check if the two numbers are equal or not
        if (num1 == num2) {
            System.out.println("The two numbers are equal.");
        } else {
            System.out.println("The two numbers are not equal.");
        }

        // Close the scanner to prevent resource leaks
        scanner.close();
    }
}
