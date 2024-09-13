import java.util.HashSet;
import java.util.Set;

public class ArrayDuplicates {
    public static int[] findDuplicates(int[] arr) {
        Set<Integer> seen = new HashSet<>();
        Set<Integer> duplicates = new HashSet<>();

        for (int num : arr) {
            if (!seen.add(num)) {
                duplicates.add(num);
            }
        }

        int[] duplicateArray = new int[duplicates.size()];
        int i = 0;
        for (int num : duplicates) {
            duplicateArray[i++] = num;
        }

        return duplicateArray;
    }

    public static void main(String[] args) {
        int[] numbers = {10, 20, 30, 20, 40, 30, 50};
        int[] duplicates = findDuplicates(numbers);

        System.out.print("Duplicate values: ");
        for (int num : duplicates) {
            System.out.print(num + " ");
        }
    }
}