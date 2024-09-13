public class EvenOddCounter {

    // Method to count the number of even and odd numbers in an array
    public static int[] countEvenOdd(int[] array) {
        // Initialize counters
        int evenCount = 0;
        int oddCount = 0;

        // Iterate through the array and count even and odd numbers
        for (int num : array) {
            if (num % 2 == 0) {
                evenCount++;
            } else {
                oddCount++;
            }
        }

        // Return the counts as an array [evenCount, oddCount]
        return new int[]{evenCount, oddCount};
    }

    public static void main(String[] args) {
        // Example array
        int[] array = {12, 35, 1, 10, 34, 21, 18};

        // Get counts of even and odd numbers
        int[] counts = countEvenOdd(array);

        // Print the results
        System.out.println("Number of even numbers: " + counts[0]);
        System.out.println("Number of odd numbers: " + counts[1]);
    }
}
