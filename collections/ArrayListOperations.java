import java.util.ArrayList;
import java.util.Iterator;

public class ArrayListOperations {
    public static void main(String[] args) {
        // Create an ArrayList of type String with 10 elements
        ArrayList<String> list = new ArrayList<>();
        for (int i = 1; i <= 10; i++) {
            list.add("Element " + i);
        }

        // Add an element to the ArrayList
        list.add("New Element");  // Adds to the end of the list
        System.out.println("After adding new element: " + list);

        // Iterate through the ArrayList using Iterator
        System.out.println("Iterating through the list:");
        Iterator<String> iterator = list.iterator();
        while (iterator.hasNext()) {
            System.out.println(iterator.next());
        }

        // Add an element at a specific index
        list.add(5, "Inserted Element");  // Inserts at index 5
        System.out.println("After adding element at index 5: " + list);

        // Remove an element from the ArrayList
        list.remove("Element 3");  // Removes the first occurrence of "Element 3"
        System.out.println("After removing 'Element 3': " + list);

        // Remove an element at a specific index
        list.remove(2);  // Removes element at index 2
        System.out.println("After removing element at index 2: " + list);

        // Update the element at a specific index
        list.set(3, "Updated Element");  // Updates the element at index 3
        System.out.println("After updating element at index 3: " + list);

        // Check if an element is present at a particular index
        String elementAtIndex = list.get(3);  // Get the element at index 3
        System.out.println("Element at index 3: " + elementAtIndex);

        // Get the size of the ArrayList
        int size = list.size();
        System.out.println("Size of the ArrayList: " + size);

        // Check if a given element is present in the ArrayList
        boolean containsElement = list.contains("Updated Element");
        System.out.println("Does the list contain 'Updated Element'? " + containsElement);

        // Remove all elements of the ArrayList
        list.clear();
        System.out.println("After removing all elements: " + list);
    }
}
