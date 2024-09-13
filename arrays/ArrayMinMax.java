public class ArrayMinMax {
    public static int[] findMinMax(int[] arr) {
        if (arr.length == 0) {
            return null; // Empty array
        }

        int min = arr[0];
        int max = arr[0];

        for (int i = 1; i < arr.length; i++) {
            if (arr[i] < min) {
                min = arr[i];
            } else if (arr[i] > max) {
                max = arr[i];
            }
        }

        int[] result = {min, max};
        return result;
    }

    public static void main(String[] args) {
        int[] numbers = {10, 20, 30, 5, 45};
        int[] minMax = findMinMax(numbers);

        System.out.println("Minimum value: " + minMax[0]);
        System.out.println("Maximum value: " + minMax[1]);
    }
}