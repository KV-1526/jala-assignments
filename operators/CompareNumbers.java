import java.util.Scanner;

public class CompareNumbers {

    public static void main(String[] args) {
        // Create a Scanner object for user input
        Scanner scanner = new Scanner(System.in);

        // Prompt the user to enter two numbers
        System.out.print("Enter the first number: ");
        int num1 = scanner.nextInt();

        System.out.print("Enter the second number: ");
        int num2 = scanner.nextInt();

        // Compare the two numbers and print the smaller and larger number
        if (num1 < num2) {
            System.out.println("Smaller number: " + num1);
            System.out.println("Larger number: " + num2);
        } else if (num1 > num2) {
            System.out.println("Smaller number: " + num2);
            System.out.println("Larger number: " + num1);
        } else {
            System.out.println("Both numbers are equal.");
        }

        // Close the scanner to avoid resource leaks
        scanner.close();
    }
}
