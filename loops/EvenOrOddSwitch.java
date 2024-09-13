public class EvenOrOddSwitch {
    public static void main(String[] args) {
        int number = 15; // Replace with the number you want to check

        switch (number % 2) {
            case 0:
                System.out.println(number + " is even.");
                break;
            case 1:
                System.out.println(number + " is odd.");
                break;
            default:
                System.out.println("Invalid number.");
        }
    }
}