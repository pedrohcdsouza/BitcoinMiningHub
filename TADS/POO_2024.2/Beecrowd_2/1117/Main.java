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

        float n1 = sc.nextFloat();

        if(n1 > 10 || n1 < 0){
            System.out.println("nota invalida");
        } else; float n2 = sc.nextFloat();

        if(n2 > 10 || n2 < 0){
            System.out.println("nota invalida");
        } else{
            System.out.println("media = " + (n1+n2)/2);
        }

    }
}
