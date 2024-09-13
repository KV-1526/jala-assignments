public class ArrayInsert {
    public static int[] insertElement(int[] arr, int element, int index) {
        int[] result = new int[arr.length + 1];

        System.arraycopy(arr, 0, result, 0, index);
        result[index] = element;
        System.arraycopy(arr, index, result, index + 1, arr.length - index);

        return result;
    }

    public static void main(String[] args) {
        int[] numbers = {10, 20, 30, 40, 50};
        int element = 25;
        int index = 2;

        int[] modifiedArray = insertElement(numbers, element, index);

        System.out.print("Modified array: ");
        for (int num : modifiedArray) {
            System.out.print(num + " ");
        }
    }
}