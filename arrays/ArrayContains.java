public class ArrayContains {
    public static boolean contains(int[] arr, int target) {
        for (int num : arr) {
            if (num == target) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        int[] numbers = {10, 20, 30, 40, 50};
        int target = 30;

        if (contains(numbers, target)) {
            System.out.println("The array contains " + target);
        } else {
            System.out.println("The array does not contain " + target);
        }
    }
}