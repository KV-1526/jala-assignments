public class task3 {
    public static void main(String[] args) {
        // This is a single-line comment
        System.out.println("Hello, World!");  // Another single-line comment

        /*
         * This is a multi-line comment.
         * It can span multiple lines.
         * This program prints a message to the console.
         */
        System.out.println("Java Comments Example");

        /**
         * This is a documentation comment.
         * It is used to describe classes, methods, and variables in detail.
         * You can generate HTML documentation using the javadoc tool.
         */
        printMessage();
    }

    /**
     * This method prints a message to the console.
     * This is a documentation comment used for JavaDocs.
     */
    public static void printMessage() {
        System.out.println("This is a message from the printMessage method.");
    }
}
