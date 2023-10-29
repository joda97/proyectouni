from modulos.Cliente import *
from modulos.Inventario import *

class Pedido:

    __cliente = None

    __listaProductos = []

    __costoTotal = 0.0

    __resumen = ""

    def __init__(self, inventario):

        nombre = input("\nIngrese el nombre del cliente a registrar: ")
        
        self.__cliente = Cliente(nombre,
                               input(f"\nIngrese la direccion de {nombre}: "),
                               input(f"\nIngrese el correo electronico de {nombre}: "))
        
        respuesta = "S"

        self.__listaProductos = []

        self.__costoTotal = 0.0

        self.resumen = f"\nNombre: {self.__cliente.getNombre()}" + f"\nDireccion: {self.__cliente.getDireccion()}" + f"\nCorreo Electronico: {self.__cliente.getEmail()}\n"

        while respuesta == "S" and len(self.__listaProductos) < len(inventario.getProductos()):

            encuentra = False

            nombreProducto = input("\nIngrese el nombre del producto: ")

            for i in inventario.getProductos():

                if (i.getNombre()).upper() == nombreProducto.upper():

                    encuentra = True

                    self.__listaProductos.append(i)

                    cantidadProducto = int(input(f"\nCuantos {nombreProducto.capitalize()} desea agregar?: "))

                    while cantidadProducto > i.getCantidad():

                        cantidadProducto = int(input(f"\nLo siento solo contamos con {i.getCantidad()} en inventario, ingrese la cantidad que desee agregar: "))

                    self.__costoTotal += (i.getPrecio() * cantidadProducto)

                    self.resumen += f"\n* {nombreProducto.capitalize()}  {i.getPrecio()} X {cantidadProducto} = {i.getPrecio() * cantidadProducto}"

                    break

            while encuentra == False:

                nombreProducto = input("\nEl nombre ingresado no coincide con ningun producto del inventario, ingrese nuevamente el nombre: ")

                for i in inventario.getProductos():

                    if (i.getNombre()).upper() == nombreProducto.upper():

                        encuentra = True

                        self.__listaProductos.append(i)

                        cantidadProducto = int(input(f"\nCuantos {nombreProducto.capitalize()} desea agregar?: "))

                        while cantidadProducto > i.getCantidad():

                            cantidadProducto = int(input(f"\nLo siento solo contamos con {i.getCantidad()} en inventario, ingrese la cantidad que desee agregar: "))

                        self.__costoTotal += (i.getPrecio() * cantidadProducto)

                        self.resumen += f"\n* {nombreProducto.capitalize()}  {i.getPrecio()} X {cantidadProducto} = {i.getPrecio() * cantidadProducto}"

                        break
                
            respuesta = (input("\nDesea agregar otro producto? (S/N): ")).upper()

            while respuesta != "S" and respuesta != "N":

                respuesta = (input("\nSolo ingrese (S/N): ")).upper()

    def agregarProducto(self, inventario):

        respuesta = "S"

        while respuesta == "S" and len(self.__listaProductos) < len(inventario.getProductos()):

            encuentra = False

            nombreProducto = input("\nIngrese el nombre del producto: ")

            for i in inventario.getProductos():

                if (i.getNombre()).upper() == nombreProducto.upper():

                    encuentra = True

                    self.__listaProductos.append(i)

                    cantidadProducto = int(input(f"\nCuantos {nombreProducto} desea agregar?: "))

                    while cantidadProducto > i.getCantidad():

                        cantidadProducto = int(input(f"\nLo siento solo contamos con {i.getCantidad()} en inventario, ingrese la cantidad que desee agregar: "))

                    self.__costoTotal += (i.getPrecio() * cantidadProducto)

                    self.resumen += f"\n* {nombreProducto}  {i.getPrecio()} X {cantidadProducto} = {i.getPrecio() * cantidadProducto}"

                    break

            while encuentra == False:

                nombreProducto = input("\nEl nombre ingresado no coincide con ningun producto del invetario, ingrese nuevamente el nombre: ")

                for i in inventario.getProductos():

                    if (i.getNombre()).upper() == nombreProducto.upper():

                        encuentra = True

                        self.__listaProductos.append(i)

                        cantidadProducto = int(input(f"\nCuantos {nombreProducto} desea agregar?: "))

                        while cantidadProducto > i.getCantidad():

                            cantidadProducto = int(input(f"\nLo siento solo contamos con {i.getCantidad()} en inventario, ingrese la cantidad que desee agregar: "))

                        self.__costoTotal += (i.getPrecio() * cantidadProducto)

                        self.resumen += f"\n* {nombreProducto}  {i.getPrecio()} X {cantidadProducto} = {i.getPrecio() * cantidadProducto}"

                        break

            respuesta = (input("\nDesea agregar otro producto? (S/N): ")).upper()

            while respuesta != "S" and respuesta != "N":

                respuesta = (input("\nSolo ingrese (S/N): ")).upper()

    def setDireccion(self):

        self.__cliente.setDireccion(input("\nIngrese la nueva direccion de entrega: "))

    def setEmail(self):

        self.__cliente.setEmail(input("Ingrese el nuevo correo electronico: "))

    def getNombreCliente(self):
    
        return self.__cliente.getNombre()
    
    def getResumen(self):

        return self.resumen + f"\n\nTotal = {self.__costoTotal}"
    
    def getListaProductos(self):

        return self.__listaProductos