public class GenderSwitch {
    public static void main(String[] args) {
        char gender = 'F'; // Replace with 'M' or 'F'

        switch (gender) {
            case 'M':
                System.out.println("Male");
                break;
            case 'F':
                System.out.println("Female");
                break;
            default:
                System.out.println("Invalid gender.");
        }
    }
}