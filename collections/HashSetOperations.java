import java.util.HashSet;
import java.util.Iterator;

public class HashSetOperations {
    public static void main(String[] args) {
        // Create a HashSet with at least 10 elements
        HashSet<String> set = new HashSet<>();
        set.add("Apple");
        set.add("Banana");
        set.add("Cherry");
        set.add("Date");
        set.add("Elderberry");
        set.add("Fig");
        set.add("Grape");
        set.add("Honeydew");
        set.add("Kiwi");
        set.add("Lemon");

        // Add an element to the HashSet
        set.add("Mango");
        System.out.println("After adding Mango: " + set);

        // Remove a specific element from the HashSet
        set.remove("Date");
        System.out.println("After removing Date: " + set);

        // Check if the HashSet contains a specific element
        boolean containsElement = set.contains("Fig");
        System.out.println("Does the set contain Fig? " + containsElement);

        // Get the size of the HashSet
        int size = set.size();
        System.out.println("Size of the HashSet: " + size);

        // Check if the HashSet is empty
        boolean isEmpty = set.isEmpty();
        System.out.println("Is the HashSet empty? " + isEmpty);

        // Print all elements using an iterator
        System.out.println("Iterating through the HashSet:");
        Iterator<String> iterator = set.iterator();
        while (iterator.hasNext()) {
            System.out.println(iterator.next());
        }

        // Print all elements using a for-each loop
        System.out.println("Printing all elements using for-each loop:");
        for (String element : set) {
            System.out.println(element);
        }

        // Clear all elements from the HashSet
        set.clear();
        System.out.println("After clearing the HashSet: " + set);
    }
}
