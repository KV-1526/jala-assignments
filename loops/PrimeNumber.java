public class PrimeNumber {

    public static void main(String[] args) {
        int number = 13; // Replace with the number you want to check

        if (number <= 1) {
            System.out.println(number + " is not a prime number.");
            return;
        }

        // Efficiently check for divisibility up to the square root of the number
        int limit = (int) Math.sqrt(number);
        for (int i = 2; i <= limit; i++) {
            if (number % i == 0) {
                System.out.println(number + " is not a prime number.");
                return;
            }
        }

        System.out.println(number + " is a prime number.");
    }
}