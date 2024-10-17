package Examples;

public class switchTest {

    public static int monthDays(int month) {
        return month == 1 || month == 3 || month == 5 || month == 7 || month == 9 || month == 11 ? 31
        : month == 4 || month == 6 || month == 8 || month == 10 || month == 12 ? 30
        : 28;
    }
    
    public static void main(String[] args) {
    
        int month = 2;
        int days = monthDays(month);
        System.out.println(days);
    
    }
}