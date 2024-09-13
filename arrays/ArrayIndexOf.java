public class ArrayIndexOf {
    public static int findIndexOf(int[] arr, int target) {
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
        int index = findIndexOf(numbers, target);

        if (index != -1) {
            System.out.println("The index of " + target + " is: " + index);
        } else {
            System.out.println("The element " + target + " is not found in the array.");
        }
    }
}