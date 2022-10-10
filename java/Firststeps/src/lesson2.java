public class lesson2 {
    public static void main (String[] args) {
       yesloop();
       carloop();
       day();
       switchday();
       tryexcept();

    }

    public static void yesloop(){
        for (int i=0; i <5; i++){
            System.out.println("Yes");
        }
    }

    public static void carloop(){
        String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
        for (String el : cars ) {
            System.out.println(el);
        }
    }

    public static void day(){
        int day = 4;
                if (day == 6){
                    System.out.println("today is Saturday");
                }
                else if (day == 7){
                    System.out.println("today is Sunday");
                }
                else{
                    System.out.println("looking forward to the weekend");
                }
    }

    public static void switchday(){
        switch (int day = 4) {
            case 6:
                System.out.println("today is Saturday");
                break;
            case 7:
                System.out.println("today is Sunday");
                break;
            default:
                System.out.println("looking forward to the weekend");
        }

    }

    public static void tryexcept();


}
