public class ArrayElementVerifier {

    // Method to check if the array contains both specified elements
    public static boolean containsBothElements(int[] array, int elem1, int elem2) {
        boolean foundElem1 = false;
        boolean foundElem2 = false;

        // Iterate through the array to check for the presence of both elements
        for (int num : array) {
            if (num == elem1) {
                foundElem1 = true;
            }
            if (num == elem2) {
                foundElem2 = true;
            }
            // If both elements are found, no need to check further
            if (foundElem1 && foundElem2) {
                return true;
            }
        }

        // Return true if both elements are found, otherwise false
        return foundElem1 && foundElem2;
    }

    public static void main(String[] args) {
        // Example array
        int[] array = {5, 12, 7, 23, 34, 18};

        // Specify the elements to check for
        int element1 = 12;
        int element2 = 23;

        // Check if the array contains both specified elements
        boolean result = containsBothElements(array, element1, element2);

        // Print the result
        if (result) {
            System.out.println("The array contains both " + element1 + " and " + element2 + ".");
        } else {
            System.out.println("The array does not contain both " + element1 + " and " + element2 + ".");
        }
    }
}
