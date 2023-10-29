from modulos.Tienda import *

respuesta = "N"

tiendaOnline = Tienda()

while respuesta == "N":

    opcionGestion = int(input("\nQue desea gestionar?:\n"
                              "\n1- Inventario"
                              "\n2- Clientes"
                              "\n3- Cerrar\n"
                              "\nIngrese el numero de la opcion que desee: "))

    while opcionGestion < 1 or opcionGestion > 3:

        opcionGestion = int(input("\nOpcion no valida, que desea gestionar?:\n"
                                  "\n1- Inventario"
                                  "\n2- Clientes"
                                  "\n3- Cerrar\n"
                                  "\nIngrese el numero de la opcion que desee: "))
        
    if opcionGestion == 1:

        opcionInventario = int(input("\nQue desea hacer?:\n"
                                     "\n1- Agregar un producto"
                                     "\n2- Cambiar la cantidad de un producto"
                                     "\n3- Cambiar el precio de un prodcuto"
                                     "\n4- Ver el informe especifico de un producto"
                                     "\n5- Ver el informe general del inventario\n"
                                     "\nIngrese el numero de la opcion que desee: "))
        
        while opcionInventario < 1 or opcionInventario > 5:

            opcionInventario = int(input("\nOpcion no valida, que desea hacer?:\n"
                                         "\n1- Agregar un producto"
                                         "\n2- Cambiar la cantidad de un producto"
                                         "\n3- Cambiar el precio de un prodcuto"
                                         "\n4- Ver el informe especifico de un producto"
                                         "\n5- Ver el informe general del inventario\n"
                                         "\nIngrese el numero de la opcion que desee: "))
            
        if opcionInventario == 1:

            tiendaOnline.agregarProducto()

        elif opcionInventario == 2:

            tiendaOnline.cambiarCantidad()

        elif opcionInventario == 3:

            tiendaOnline.cambiarPrecio()

        elif opcionInventario == 4:

            tiendaOnline.generarInformeEspecifico()

        else:

            tiendaOnline.generarInformeGeneral()

    elif opcionGestion == 2:

        opcionCliente = int(input("\nQue desea hacer?:\n"
                                  "\n1- Agregar a un cliente"
                                  "\n2- Gestionar a un cliente\n"
                                  "\nIngrese el numero de la opcion que desee: "))
        
        while opcionCliente < 1 or opcionCliente > 2:

            opcionCliente = int(input("\nQue desea hacer?:\n"
                                      "\n1- Agregar a un cliente"
                                      "\n2- Gestionar a un cliente\n"
                                      "\nIngrese el numero de la opcion que desee: "))
            
        if opcionCliente == 1:

            tiendaOnline.agregarPedido()

        else:

            tiendaOnline.gestionarPedido()

    else:

        break

    respuesta = (input("\nDesea cerrar el programa? (S/N): ")).upper()

    while respuesta != "S" and respuesta != "N":

        respuesta = (input("\nSolo ingrese (S/N): ")).upper()