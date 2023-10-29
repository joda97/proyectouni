class Producto:

    __nombre = ""

    __precio = 0.0

    __cantidad = 0

    def __init__(self, nombre, precio, cantidad):

        self.__nombre = nombre

        self.__precio = precio

        self.__cantidad = cantidad

    def setPrecio(self, precio):

        self.__precio = precio

    def setCantidad(self, cantidad):

        self.__cantidad = cantidad

    def getNombre(self):

        return self.__nombre
    
    def getPrecio(self):

        return self.__precio
    
    def getCantidad(self):
    
        return self.__cantidad