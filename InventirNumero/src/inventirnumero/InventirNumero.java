package inventirnumero;

import java.util.Scanner;

public class InventirNumero {

    public static void main(String[] args) {
        
        Scanner teclado = new Scanner(System.in);
        
        System.out.print("Ingrese un numero entero de 5 cifras: ");
        
        String numero = teclado.nextLine();
        
        System.out.println();
        
        for(int i = 5; i > 0; i--){
        
            System.out.println(numero.charAt(i - 1));
        
        }
        
    }
    
}
