package calculadorcosto;

import java.util.Scanner;

public class CalculadorCosto {

    public static void main(String[] args) {
        
        Scanner teclado = new Scanner(System.in);
        
        String respuesta = "S";
        
        float porcentaje = 1F;
        
        float precioVenta;
        
        do{
            
            System.out.print("\nIngrese el precio costo de su producto: ");
        
            float precioCosto = teclado.nextFloat();
            
            if (precioCosto >= 100){
            
                porcentaje = 0.30F;
            
            }
            
            else if (precioCosto >= 60){
            
               porcentaje = 0.45F;
            
            }
            
            else if(precioCosto > 0){
        
                porcentaje = 0.70F;
        
            }
            
            precioVenta = (float) ((precioCosto) + (precioCosto * 1.16) + (precioCosto * porcentaje));
        //% formateo .2 indica la cantidad de decimales y f indica que es float 
            System.out.printf("\nEl precio de venta sera de %.2f$.", precioVenta);
        //eso me lo dijo Jose
            teclado.nextLine();
            
            System.out.print("\n\nDesea costear otro producto(S/N): ");
            
            respuesta = teclado.nextLine();
        
        }while (respuesta.equalsIgnoreCase("S"));
        
    }
    
}
