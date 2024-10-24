import java.io.IOException;
import java.util.Scanner;

/**
 * IMPORTANT: 
 *      O nome da classe deve ser "Main" para que a sua solução execute
 *      Class name must be "Main" for your solution to execute
 *      El nombre de la clase debe ser "Main" para que su solución ejecutar
 */
public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner sc = new Scanner(System.in);
        long highest = 0;
        int position = 0;

        for(int x = 0; x <= 100; x++){
            long value = sc.nextLong();
            if(value > highest){
                highest = value;
                position = x;
            }
        }
        System.out.println(highest);
        System.out.println(position);
    }
}