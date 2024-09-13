public class GenerateArrayIndexOutOfBoundsException {
    public static void main(String[] args) {
        int[] numbers = {1, 2, 3}; // Array with 3 elements

        // Attempting to access an index that is out of bounds
        int invalidIndex = 5; // Index 5 is out of bounds for an array of size 3

        // This will cause ArrayIndexOutOfBoundsException
        int result = numbers[invalidIndex];

        // This line will not be executed because the exception is thrown above
        System.out.println("Element at index " + invalidIndex + ": " + result);
    }
}
