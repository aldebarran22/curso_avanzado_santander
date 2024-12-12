"""
Implementación del patrón Builder para convertir el formato
de un fichero CSV a:
- Json -> BuilderJSON
- XML -> BuilderXML
- HTML -> BuilderHTML
"""

import abc

class Builder(abc.ABC):

    @abc.abstractmethod
    def generarCabecera(self, L):
        pass

    @abc.abstractmethod
    def generarDetalle(self, L):
        pass

    @abc.abstractmethod
    def grabarFichero(self, tabla, path):
        pass

class BuilderHTML(Builder):

    def generarCabecera(self, L):
        pass

    
    def generarDetalle(self, L):
        pass

   
    def grabarFichero(self, tabla, path):
        pass

class Director:

    def __init__(self, builder):
        self.builder = builder

    def build(self, pathOrigen):
        fich = None
        try:
            fich = open(pathOrigen, 'r')
            for fila in fich:
                fila = fila.rstrip()
                print(fila)

        except Exception as e:
            raise e
        finally:
            if fich:
                fich.close()

class BuilderXML(Builder):
    pass

class BuilderJSON(Builder):
    pass

if __name__ == '__main__':
    builder = BuilderHTML()
    director = Director(builder)
    director.build("origen/Empleados.txt")
