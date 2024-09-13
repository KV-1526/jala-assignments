public class ArrayRemove {
    public static int[] removeElement(int[] arr, int target) {
        int index = findIndexOf(arr, target);
        if (index == -1) {
            return arr; // Target not found, return original array
        }

        int[] result = new int[arr.length - 1];
        System.arraycopy(arr, 0, result, 0, index);
        System.arraycopy(arr, index + 1, result, index, arr.length - index - 1);
        return result;
    }

    private static int findIndexOf(int[] arr, int target) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == target) {
                return i;
            }
        }
        return -1; // Target not found
    }

    public static void main(String[] args) {
        int[] numbers = {10, 20, 30, 40, 50};
        int target = 30;

        int[] modifiedArray = removeElement(numbers, target);

        System.out.print("Modified array: ");
        for (int num : modifiedArray) {
            System.out.print(num + " ");
        }
    }
}