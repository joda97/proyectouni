class Cliente:

    __nombre = ""

    __direccion = ""

    __email = ""

    def __init__(self, nombre, dirceccion, email):

        self.__nombre = nombre

        self.__direccion = dirceccion

        self.__email = email

    def setDireccion(self, direccion):

        self.__direccion = direccion

    def setEmail(self, email):

        self.__email = email

    def getNombre(self):

        return self.__nombre
    
    def getDireccion(self):

        return self.__direccion
    
    def getEmail(self):

        return self.__email