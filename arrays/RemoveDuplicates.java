import java.util.Arrays;
import java.util.HashSet;

public class RemoveDuplicates {

    // Method to remove duplicate elements from an array
    public static int[] removeDuplicates(int[] array) {
        // Create a HashSet to store unique elements
        HashSet<Integer> set = new HashSet<>();
        
        // Add all elements of the array to the HashSet
        for (int num : array) {
            set.add(num);
        }
        
        // Convert the HashSet back to an array
        int[] uniqueArray = new int[set.size()];
        int index = 0;
        for (int num : set) {
            uniqueArray[index++] = num;
        }
        
        return uniqueArray;
    }

    public static void main(String[] args) {
        // Example array with duplicate elements
        int[] arrayWithDuplicates = {4, 5, 6, 4, 7, 8, 6, 9, 5};
        
        // Remove duplicates
        int[] arrayWithoutDuplicates = removeDuplicates(arrayWithDuplicates);
        
        // Print the array without duplicates
        System.out.println("Array without duplicates: " + Arrays.toString(arrayWithoutDuplicates));
    }
}
