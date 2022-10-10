public class HelloWorld {
    public static void main (String[] args) {
        System.out.println("Hello, World!");
        not_main();
        string();
        int_str();
    }
    public static void not_main() {
        System.out.println("Hello, other method!");
    }

    public static void string() {
        String s1 = new String("Heap string, ");
        String s2 = "pool string!";
        String s3 = s1 + s2;
                System.out.println(s3);

    }

    public static void int_str() {
        int num = 5;
        String s = "I have " + num + " cookies";
        System.out.println(s);

    }

}

