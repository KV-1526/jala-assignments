import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class HashMapOperations {
    public static void main(String[] args) {
        // Create a HashMap with at least 10 key-value pairs
        HashMap<String, String> studentMap = new HashMap<>();
        studentMap.put("S001", "Alice");
        studentMap.put("S002", "Bob");
        studentMap.put("S003", "Charlie");
        studentMap.put("S004", "David");
        studentMap.put("S005", "Eva");
        studentMap.put("S006", "Frank");
        studentMap.put("S007", "Grace");
        studentMap.put("S008", "Hannah");
        studentMap.put("S009", "Ivy");
        studentMap.put("S010", "Jack");

        // Insert a key-value mapping into the map
        studentMap.put("S011", "Karen");
        System.out.println("After adding S011: " + studentMap);

        // Fetch the value of a key
        String name = studentMap.get("S005");
        System.out.println("The name associated with S005: " + name);

        // Create a clone/copy of the HashMap
        HashMap<String, String> clonedMap = (HashMap<String, String>) studentMap.clone();
        System.out.println("Cloned map: " + clonedMap);

        // Check if the given key is in the map
        boolean hasKey = studentMap.containsKey("S007");
        System.out.println("Does the map contain S007? " + hasKey);

        // Check if the value is in the map
        boolean hasValue = studentMap.containsValue("Charlie");
        System.out.println("Does the map contain value 'Charlie'? " + hasValue);

        // Check if the map is empty
        boolean isEmpty = studentMap.isEmpty();
        System.out.println("Is the map empty? " + isEmpty);

        // Print the size of the map
        int size = studentMap.size();
        System.out.println("Size of the map: " + size);

        // Print all the keys of the map
        System.out.println("Keys of the map: " + studentMap.keySet());

        // Print all the values of the map
        System.out.println("Values of the map: " + studentMap.values());

        // Remove a specific key-value pair
        studentMap.remove("S003");
        System.out.println("After removing S003: " + studentMap);

        // Copy all the elements of the map to another map
        HashMap<String, String> anotherMap = new HashMap<>(studentMap);
        System.out.println("Another map (copied): " + anotherMap);
    }
}
