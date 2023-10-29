from modulos.Producto import *

class Inventario:

    __productos = []

    def __init__(self):
        
        self.__productos = []

    def agregarProducto(self):

        nombre = input("\nIngrese el nombre del producto a agregar: ")

        self.__productos.append(Producto(nombre,
                                       float(input(f"\nIngrese el precio de {nombre}: ")),
                                       int(input(f"\nIngrese la cantidad de {nombre}: "))))
        
    def cambiarPrecio(self):

        encuentra = False

        nombre = input("\nIngrese el nombre del producto: ")

        for i in self.__productos:

            if (i.getNombre()).upper() == nombre.upper():

                precio = float(input(f"\nIngrese el nuevo precio de {nombre}: "))

                while precio == i.getPrecio():

                    precio = float(input(f"\nEl precio ya es el establecido, ingrese el nuevo precio de {nombre}: "))

                i.setPrecio(precio)

                encuentra = True

                break
        
        while encuentra == False:

            nombre = input("\nEL nombre ingresado no se encuentra registrado, ingrese el nombre del producto: ")

            for i in self.__productos:

                if (i.getNombre()).upper() == nombre.upper():

                    precio = float(input(f"\nIngrese el nuevo precio de {nombre}: "))

                    while precio == i.getPrecio():

                        precio = float(input(f"\nEl precio ya es el establecido, ingrese el nuevo precio de {nombre}: "))

                    i.setPrecio(precio)

                    encuentra = True

                    break

    def cambiarCantidad(self):

        encuentra = False

        nombre = input("\nIngrese el nombre del producto: ")

        for i in self.__productos:
        
            if (i.getNombre()).upper() == nombre.upper():

                cantidad = int(input(f"\nIngrese la nueva cantidad de {nombre}: "))

                while cantidad == i.getCantidad():

                    cantidad = int(input(f"\nLa cantidad ya es la establecida, ingrese la nueva cantidad de {nombre}: "))

                i.setCantidad(cantidad)

                encuentra = True

                break

        while encuentra == False:

            nombre = input("\nEl nombre ingresado no se encuentra registado, ingrese el nombre del producto: ")

            for i in self.__productos:
        
                if (i.getNombre()).upper() == nombre.upper():

                    cantidad = int(input(f"Ingrese la nueva cantidad de {nombre}: "))

                    while cantidad == i.getCantidad():

                        cantidad = int(input(f"\nLa cantidad ya es la establecida, ingrese la nueva cantidad de {nombre}: "))

                    i.setCantidad(cantidad)

                    encuentra = True

                    break

    def generarInformeEspecifico(self):
        
        encuentra = False

        nombre = input("\nIngrese el nombre del producto: ")

        for i in self.__productos:

            if (i.getNombre()).upper() == nombre.upper():

                print(f"\nProducto: {i.getNombre()}"
                      f"\nPrecio: {i.getPrecio()}"
                      f"\nCantidad: {i.getCantidad()}")

                encuentra = True

                break

        while encuentra == False:

            nombre = input("\nEl nombre ingresado no se encuentra registrado, ingrese el nombre del producto: ")

            for i in self.__productos:

                if (i.getNombre()).upper() == nombre.upper():

                    print(f"\nProducto: {i.getNombre()}"
                          f"\nPrecio: {i.getPrecio()}"
                          f"\nCantidad: {i.getCantidad()}")

                    encuentra = True

                    break

    def generarInformeGeneral(self):

        print("\nInforme General del Inventario: ")

        numero = 1

        for i in self.__productos:

            print(f"\n{numero})  Nombre: {i.getNombre()}"
                  f"\n    Precio: {i.getPrecio()}"
                  f"\n    Cantidad: {i.getCantidad()}")

            numero += 1
                
    def getProductos(self):

        return self.__productos