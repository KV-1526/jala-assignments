public class DifferenceBetweenExtremes {

    // Method to find the difference between the largest and smallest values in an array
    public static int differenceBetweenLargestAndSmallest(int[] array) {
        if (array == null || array.length == 0) {
            throw new IllegalArgumentException("Array must contain at least one element.");
        }

        // Initialize the smallest and largest variables
        int smallest = array[0];
        int largest = array[0];

        // Iterate through the array to find the smallest and largest values
        for (int num : array) {
            if (num < smallest) {
                smallest = num;
            }
            if (num > largest) {
                largest = num;
            }
        }

        // Return the difference between the largest and smallest values
        return largest - smallest;
    }

    public static void main(String[] args) {
        // Example array
        int[] array = {12, 35, 1, 10, 34, 21, 18};

        try {
            // Get the difference between the largest and smallest values
            int difference = differenceBetweenLargestAndSmallest(array);
            System.out.println("The difference between the largest and smallest values is: " + difference);
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
        }
    }
}
