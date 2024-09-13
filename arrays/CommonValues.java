import java.util.HashSet;
import java.util.Set;

public class CommonValues {
    public static int[] findCommonValues(int[] arr1, int[] arr2) {
        Set<Integer> set1 = new HashSet<>();
        for (int num : arr1) {
            set1.add(num);
        }

        Set<Integer> common = new HashSet<>();
        for (int num : arr2) {
            if (set1.contains(num)) {
                common.add(num);
            }
        }

        int[] commonArray = new int[common.size()];
        int i = 0;
        for (int num : common) {
            commonArray[i++] = num;
        }

        return commonArray;
    }

    public static void main(String[] args) {
        int[] array1 = {10, 20, 30, 40, 50};
        int[] array2 = {30, 40, 60, 70};

        int[] common = findCommonValues(array1, array2);

        System.out.print("Common values: ");
        for (int num : common) {
            System.out.print(num + " ");
        }
    }
}