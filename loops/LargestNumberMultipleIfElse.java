public class LargestNumberMultipleIfElse {
    public static void main(String[] args) {
        int num1 = 10;
        int num2 = 20;
        int num3 = 30;

        if (num1 > num2 && num1 > num3) {
            System.out.println("num1 (" + num1 + ") is the largest.");
        } else if (num2 > num1 && num2 > num3) {
            System.out.println("num2 (" + num2 + ") is the largest.");
        } else if (num3 > num1 && num3 > num2) {
            System.out.println("num3 (" + num3 + ") is the largest.");
        } else {
            System.out.println("At least two numbers are equal.");
        }
    }
}