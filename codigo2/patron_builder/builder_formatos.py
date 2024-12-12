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
        pass

class BuilderXML(Builder):
    pass

class BuilderJSON(Builder):
    pass

if __name__ == '__main__':
    builder = BuilderJSON()
    director = Director(builder)
    director.build()
