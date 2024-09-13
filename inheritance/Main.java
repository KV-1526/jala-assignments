// Superclass A
class A {
    // Method specific to class A
    void methodA1() {
        System.out.println("Method A1 in class A");
    }

    // Method specific to class A
    void methodA2() {
        System.out.println("Method A2 in class A");
    }

    // Overridden method
    void overriddenMethod() {
        System.out.println("Overridden method in class A");
    }
}

// Subclass B (extends A)
class B extends A {
    // Method specific to class B
    void methodB1() {
        System.out.println("Method B1 in class B");
    }

    // Method specific to class B
    void methodB2() {
        System.out.println("Method B2 in class B");
    }

    // Overridden method
    @Override
    void overriddenMethod() {
        System.out.println("Overridden method in class B");
    }
}

// Subclass C (extends B)
class C extends B {
    // Method specific to class C
    void methodC1() {
        System.out.println("Method C1 in class C");
    }

    // Method specific to class C
    void methodC2() {
        System.out.println("Method C2 in class C");
    }

    // Overridden method
    @Override
    void overriddenMethod() {
        System.out.println("Overridden method in class C");
    }
}

// Main class to demonstrate method calls and runtime polymorphism
public class Main {
    public static void main(String[] args) {
        // Create instances of each class
        A a = new A();
        B b = new B();
        C c = new C();

        // Call methods on instances of class A
        System.out.println("Calling methods on object of class A:");
        a.methodA1();
        a.methodA2();
        a.overriddenMethod();

        // Call methods on instances of class B
        System.out.println("\nCalling methods on object of class B:");
        b.methodA1(); // Inherited from A
        b.methodA2(); // Inherited from A
        b.methodB1();
        b.methodB2();
        b.overriddenMethod();

        // Call methods on instances of class C
        System.out.println("\nCalling methods on object of class C:");
        c.methodA1(); // Inherited from A
        c.methodA2(); // Inherited from A
        c.methodB1(); // Inherited from B
        c.methodB2(); // Inherited from B
        c.methodC1();
        c.methodC2();
        c.overriddenMethod();

        // Demonstrate runtime polymorphism
        System.out.println("\nDemonstrating runtime polymorphism:");
        A aRef;
        
        // A reference to an object of B
        aRef = b;
        aRef.overriddenMethod(); // Calls overridden method in B
        
        // A reference to an object of C
        aRef = c;
        aRef.overriddenMethod(); // Calls overridden method in C
    }
}
