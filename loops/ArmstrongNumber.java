public class ArmstrongNumber {
    public static void main(String[] args) {
        int number = 153; // Replace with the number you want to check
        int originalNumber = number;
        int result = 0;
        int n = String.valueOf(number).length();

        while (number != 0) {
            int remainder = number % 10;
            result += Math.pow(remainder, n);
            number /= 10;
        }

        if (originalNumber == result) {
            System.out.println(originalNumber + " is an Armstrong number.");
        } else {
            System.out.println(originalNumber + " is not an Armstrong number.");
        }
    }
}