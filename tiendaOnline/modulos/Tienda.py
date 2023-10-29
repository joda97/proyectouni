from modulos.Inventario import *
from modulos.Pedido import *

class Tienda:

    __inventario = None

    __listaPedidos = []

    def __init__(self):

        self.__inventario = Inventario()

        self.__listaPedidos = []

    def agregarPedido(self):

        if len(self.__inventario.getProductos()) >= 1:

            self.__listaPedidos.append(Pedido(self.__inventario))

        else:

            print("\nNo hay productos en el inventario.")

    def gestionarPedido(self):

        if len(self.__listaPedidos) >= 1:

            encuentra  = False

            nombreCliente = input("\nIngrese el nombre del cliente que busca: ")

            for i in self.__listaPedidos:

                if nombreCliente.upper() == (i.getNombreCliente()).upper():

                    opcion = int(input("\nQue desea hacer?:\n"
                                     + "\n1- Agregar Productos"
                                     + "\n2- Ver Resumen"
                                     + "\n3- Cambiar la direccion"
                                     + "\n4- Cambiar el e-mail\n"
                                     + "\nIngrese el numero de la opcion que desee realizar: "))

                    while opcion < 1 or opcion > 4:

                        opcion = int(input("\nOpcion no valida, que desea hacer?:\n"
                                         + "\n1- Agregar Productos"
                                         + "\n2- Ver Resumen"
                                         + "\n3- Cambiar la direccion"
                                         + "\n4- Cambiar el e-mail\n"
                                         + "\nIngrese el numero de la opcion que desee realizar: "))

                    if opcion == 1:

                        if len(i.getListaProductos()) < len(self.__inventario.getProductos()):
                            
                            i.agregarProducto(self.__inventario)

                        else:

                            print("\nNo hay mas productos que agregar.")

                    elif opcion == 2:

                        print(i.getResumen())

                    elif opcion == 3:

                        i.setDireccion()

                    else:

                        i.setEmail()

                    encuentra = True

                    break

            while encuentra == False:

                nombreCliente = input("\nEl nombre ingresado no pretenece a un cliente registrado, Ingrese el nombre del cliente que busca: ")

                for i in self.__listaPedidos:

                    if nombreCliente.upper() == (i.getNombreCliente()).upper():

                        opcion = int(input("\nQue desea hacer?:\n"
                                         + "\n1- Agregar Productos"
                                         + "\n2- Ver Resumen"
                                         + "\n3- Cambiar la direccion"
                                         + "\n4- Cambiar el e-mail\n"
                                         + "\nIngrese el numero de la opcion que desee realizar: "))

                        while opcion < 1 or opcion > 4:

                            opcion = int(input("\nOpcion no valida, que desea hacer?:\n"
                                             + "\n1- Agregar Productos"
                                             + "\n2- Ver Resumen"
                                             + "\n3- Cambiar la direccion"
                                             + "\n4- Cambiar el e-mail\n"
                                             + "\nIngrese el numero de la opcion que desee realizar: "))

                        if opcion == 1:
                            
                            if len(i.getListaProductos()) < len(self.__inventario.getProductos()):
                            
                                i.agregarProducto(self.__inventario)

                            else:

                                print("\nNo hay mas productos que agregar.")

                        elif opcion == 2:

                            print(i.getResumen())

                        elif opcion == 3:

                            i.setDireccion()

                        else:

                            i.setEmail()

                        encuentra = True

                        break

        else:

            print("\nNo hay clientes registrados.")

    def agregarProducto(self):

        self.__inventario.agregarProducto()

    def cambiarCantidad(self):

        if len(self.__inventario.getProductos()) >= 1:

            self.__inventario.cambiarCantidad()

        else:

            print("\nNo hay productos en el inventario.")

    def cambiarPrecio(self):

        if len(self.__inventario.getProductos()) >= 1:

            self.__inventario.cambiarPrecio()

        else:

            print("\nNo hay productos en el inventario.")

    def generarInformeEspecifico(self):
            
        if len(self.__inventario.getProductos()) >= 1:

            self.__inventario.generarInformeEspecifico()

        else:

            print("\nNo hay productos en el inventario.")

    def generarInformeGeneral(self):

        if len(self.__inventario.getProductos()) >= 1:

            self.__inventario.generarInformeGeneral()

        else:

            print("\nNo hay productos en el inventario.")