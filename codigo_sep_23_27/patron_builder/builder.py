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

class BuilderHTML(Builder):
    def createCab(self, L):
        cabeceras = "".join([f"<th>{col}</th>" for col in L])
        return f"<tr>{cabeceras}</tr>"
   
    def createDetalle(self, L, etiqueta=None):
        detalle = "".join([f"<td>{col}</td>" for col in L])
        return f"<tr>{detalle}</tr>"
   
    def crearFichero(self, texto, path):
        return ""
    
class BuilderXML(Builder):

    def __init__(self):
        self.cabs = ""
        self.etiqueta = ""

    def createCab(self, L):
        self.cabs = L
        return ""

    def createDetalle(self, L, etiqueta=None):
        linea = ""
        self.etiqueta = etiqueta
        for pos, i in enumerate(L):
            linea += f"<{self.etiqueta}>{i}</{self.etiqueta}>"
        return linea

    def crearFichero(self, texto, path):
        return ""

class Director:
    """Define el proceso de creación del 
    producto final, para ello utiliza un builder."""

    def __init__(self, builder):
        self.builder = builder
        self.nombre = ""

    def convertirFichero(self, path, sep=';'):
        f = None
        cabs = True
        tabla = ""
        self.nombre = path.partition(".")[0][:-1].lower()
        try:
            f = open(path,"r")
            for linea in f:
                linea = linea.rstrip()
                L = linea.split(sep)

                if cabs:
                    tabla += self.builder.createCab(L)
                    cabs = False
                else:
                    tabla += self.builder.createDetalle(L, self.nombre)

            # crear el fichero:
            print(tabla)

        except Exception as e:
            print(e)
        finally:
            if f:f.close()


if __name__ == '__main__':
    # Seleccionar un builder según el formato destino
    builder = BuilderXML()
    director = Director(builder)
    director.convertirFichero("Empresas.txt")
