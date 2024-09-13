public class ArrayCopy {
    public static void copyArray(int[] sourceArray, int[] targetArray) {
        System.arraycopy(sourceArray, 0, targetArray, 0, sourceArray.length);
    }

    public static void main(String[] args) {
        int[] source = {10, 20, 30, 40, 50};
        int[] target = new int[source.length];

        copyArray(source, target);

        System.out.print("Copied array: ");
        for (int num : target) {
            System.out.print(num + " ");
        }
    }
}