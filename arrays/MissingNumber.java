public class MissingNumber {
    public static int findMissingNumber(int[] arr) {
        int expectedSum = (arr.length + 1) * (arr.length + 2) / 2;
        int actualSum = 0;

        for (int num : arr) {
            actualSum += num;
        }

        return expectedSum - actualSum;
    }

    public static void main(String[] args) {
        int[] numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 11}; // Missing number is 10

        int missingNumber = findMissingNumber(numbers);
        System.out.println("The missing number is: " + missingNumber);
    }
}