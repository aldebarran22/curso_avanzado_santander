"""
Implementación del patrón builder:
Objetivo convertir un fichero CSV a distintos formatos:
XML -> BuilderXML
HTML -> BuilderHTML
JSon -> BuilderJSon
"""

import abc

class Builder(abc.ABC):
    """Define las operaciones genéricas que hay que implementar
    en un builder"""

    @abc.abstractmethod
    def createCab(self, L):
        pass

    @abc.abstractmethod
    def createDetalle(self, L, etiqueta=None):
        pass

    @abc.abstractmethod
    def crearFichero(self, texto, path):
        pass

class Director:
    """Define el proceso de creación del 
    producto final, para ello utiliza un builder."""

    def __init__(self, builder):
        self.builder = builder

    def convertirFichero(self, path, sep=';'):
        f = None
        cabs = True
        tabla = ""
        try:
            f = open(path,"r")
            for linea in f:
                linea = linea.rstrip()
                L = linea.split(sep)

                if cabs:
                    tabla += self.builder.createCab(L)
                    cabs = False
                else:
                    tabla += self.builder.createDetalle(L)

            # crear el fichero:
            
        except Exception as e:
            print(e)
        finally:
            if f:f.close()
