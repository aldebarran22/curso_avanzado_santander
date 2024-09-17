"""
Patrón builder:
Conversor de formato CSV a HTML o XML
"""

import abc


class Builder(abc.ABC):

    @abc.abstractmethod
    def createCab(self, L):
        pass

    @abc.abstractmethod
    def createDetalle(self, L):
        pass

    @abc.abstractmethod
    def crearFichero(self, texto, path):
        pass


class BuilderXML(Builder):

    def createCab(self, L):
        pass

    def createDetalle(self, L):
        pass

    def crearFichero(self, texto, path):
        pass


class BuilderHTML(Builder):

    def createCab(self, L):
        pass

    def createDetalle(self, L):
        pass

    def crearFichero(self, texto, path):
        pass


class Director:

    def __init__(self, builder):
        self.builder = builder

    def convertirFichero(self, path, sep=";"):
        f = None
        nombre = path.partition(".")[0]
        try:
            f = open(path)
            for linea in f:
                linea = linea.rstrip()
                print(linea)
        except Exception as e:
            print(e)

        finally:
            if f:
                f.close()


if __name__ == "__main__":

    builder = BuilderXML()
    director = Director(builder)
    director.convertirFichero("Empleados.txt")
