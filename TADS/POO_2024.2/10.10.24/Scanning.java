import java.util.Scanner;

public class Scanning {

    public static void main(String[] args) {

        while (true) {
            Scanner myObj = new Scanner(System.in);
            System.out.println("Enter the username \n");

            String userName = myObj.nextLine();
            if (userName.equals("exit")) {
                break;
            }

            System.out.println("\nUsername is: " + userName);
        }
    }
            
}