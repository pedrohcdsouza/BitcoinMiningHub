
package Examples;
import java.util.Scanner;
 
/**
 * IMPORTANT: 
 *      O nome da classe deve ser "Main" para que a sua solução execute
 *      Class name must be "Main" for your solution to execute
 *      El nombre de la clase debe ser "Main" para que su solución ejecutar
 */
public class bhaskara {
 
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        
        double A = sc.nextDouble();
        double B = sc.nextDouble();
        double C = sc.nextDouble();

        sc.close();
        
        double delta = (B*B) - 4 * A * C;
        
        if (delta > 0) {
            double R1 = (-1 * B + Math.sqrt(delta))/2*A;
            double R2 = (-1 * B - Math.sqrt(delta))/2*A;
            System.out.println("R1 = " + R1/100);
            System.out.println("R2 = " + R2/100);
        }
        else {
            System.out.println("Impossivel calcular");
        }
        
        
    }
 
}