public class StringMatchesExample {
    public static void main(String[] args) {
        // Define some strings
        String email = "kvgowtham03@gmail.com";
        String phoneNumber = "9704205490";
        String date = "2024-08-27";
        String invalidDate = "08/27/2024";

        // Regular expression for a basic email format
        String emailRegex = "^[\\w.%+-]+@[\\w.-]+\\.[a-zA-Z]{2,}$";

        // Regular expression for a phone number format (e.g., +1-123-456-7890)
        String phoneNumberRegex = "^\\+\\d{1,3}-\\d{3}-\\d{3}-\\d{4}$";

        // Regular expression for a date in YYYY-MM-DD format
        String dateRegex = "^\\d{4}-\\d{2}-\\d{2}$";

        // Test email against the regex
        boolean isEmailValid = email.matches(emailRegex);
        System.out.println("Is email valid? " + isEmailValid);

        // Test phone number against the regex
        boolean isPhoneNumberValid = phoneNumber.matches(phoneNumberRegex);
        System.out.println("Is phone number valid? " + isPhoneNumberValid);

        // Test date against the regex
        boolean isDateValid = date.matches(dateRegex);
        System.out.println("Is date valid? " + isDateValid);

        // Test invalid date against the regex
        boolean isInvalidDateValid = invalidDate.matches(dateRegex);
        System.out.println("Is invalid date valid? " + isInvalidDateValid);
    }
}
