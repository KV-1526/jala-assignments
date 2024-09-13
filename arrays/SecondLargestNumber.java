public class SecondLargestNumber {

    // Method to find the second largest number in an array
    public static int findSecondLargest(int[] array) {
        if (array.length < 2) {
            throw new IllegalArgumentException("Array must contain at least two elements.");
        }

        // Initialize the largest and second largest numbers
        int largest = Integer.MIN_VALUE;
        int secondLargest = Integer.MIN_VALUE;

        // Iterate through the array to find the largest and second largest numbers
        for (int num : array) {
            if (num > largest) {
                secondLargest = largest; // Update second largest before updating largest
                largest = num;
            } else if (num > secondLargest && num < largest) {
                secondLargest = num;
            }
        }

        // If secondLargest is still Integer.MIN_VALUE, it means there was no valid second largest number
        if (secondLargest == Integer.MIN_VALUE) {
            throw new IllegalArgumentException("There is no distinct second largest number.");
        }

        return secondLargest;
    }

    public static void main(String[] args) {
        // Example array
        int[] array = {12, 35, 1, 10, 34, 1};

        try {
            // Find the second largest number
            int secondLargest = findSecondLargest(array);
            System.out.println("The second largest number is: " + secondLargest);
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
        }
    }
}
