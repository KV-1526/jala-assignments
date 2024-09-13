interface Drawable {
    void draw();
}

class Circle implements Drawable {
    private int radius;

    public Circle(int radius) {
        this.radius = radius;
    }

    public void draw() {
        System.out.println("Drawing a circle with radius " + radius);
    }
}

class Rectangle implements Drawable {
    private int width;
    private int height;

    public Rectangle(int width, int height) {
        this.width = width;
        this.height = height;
    }

    public void draw() {
        System.out.println("Drawing a rectangle with width " + width + " and height " + height);
    }
}

public class Main {
    public static void main(String[] args) {
        Drawable circle = new Circle(5);
        Drawable rectangle = new Rectangle(10, 20);

        drawShapes(circle, rectangle);
    }

    public static void drawShapes(Drawable... shapes) {
        for (Drawable shape : shapes) {
            shape.draw();
        }
    }
}