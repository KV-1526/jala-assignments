// Define a class
class Car {
    // Fields (attributes of the class)
    String make;
    String model;
    int year;
    
    // Constructor (special method to initialize the object)
    public Car(String make, String model, int year) {
        this.make = make;
        this.model = model;
        this.year = year;
    }

    // Method (function inside the class)
    public void displayDetails() {
        System.out.println("Car Make: " + make);
        System.out.println("Car Model: " + model);
        System.out.println("Car Year: " + year);
    }

    // Method with return type and parameters
    public int getCarAge(int currentYear) {
        return currentYear - year;
    }
}

public class task1 {
    public static void main(String[] args) {
        // Create an object of the Car class
        Car myCar = new Car("Toyota", "Camry", 2020);

        // Call methods on the object
        myCar.displayDetails();

        // Call method with parameters and capture the return value
        int carAge = myCar.getCarAge(2024);
        System.out.println("Car Age: " + carAge + " years");
    }
}
