public class ArrayReverse {
    public static void reverseArray(int[] arr) {
        int left = 0;
        int right = arr.length - 1;

        while (left < right) {
            int temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;
            left++;
            right--;
        }
    }

    public static void main(String[] args) {
        int[] numbers = {10, 20, 30, 40, 50};

        reverseArray(numbers);

        System.out.print("Reversed array: ");
        for (int num : numbers) {
            System.out.print(num + " ");
        }
    }
}