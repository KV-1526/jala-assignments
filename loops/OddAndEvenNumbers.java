public class OddAndEvenNumbers {
    public static void main(String[] args) {
        int number = 1;

        while (number <= 20) {
            if (number % 2 == 0) {
                System.out.println(number + " is even.");
            } else {
                System.out.println(number + " is odd.");
            }

            number++;
        }
    }
}