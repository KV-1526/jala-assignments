public class ArraySum {
    public static int sumArray(int[] arr) {
        int sum = 0;
        for (int num : arr) {
            sum += num;
        }
        return sum;
    }

    public static void main(String[] args) {
        int[] numbers = {10, 20, 30, 40, 50};
        int total = sumArray(numbers);
        System.out.println("The sum of the array elements is: " + total);
    }
}