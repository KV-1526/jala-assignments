public class ExceptionThrowExample {

    // Method that throws an ArithmeticException
    public static void riskyMethod() throws ArithmeticException {
        System.out.println("Inside riskyMethod.");
        throw new ArithmeticException("Exception thrown from riskyMethod");
    }

    public static void main(String[] args) {
        // Calling the method without handling the exception
        riskyMethod(); 

        // This line will not execute due to the exception thrown above
        System.out.println("This line will not be printed.");
    }
}
