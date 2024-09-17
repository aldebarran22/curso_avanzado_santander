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
        return ""

    def createDetalle(self, L):
        pass

    def crearFichero(self, texto, path):
        pass


class BuilderHTML(Builder):

    def createCab(self, L):
        """
        El formato: <tr><th>col1</th><th> ... </th></tr>
        """
        cabeceras = "".join(["<th>"+col+"</th>" for col in L])
        return "<tr>"+ cabeceras +"</tr>"

    def createDetalle(self, L):
        """
        El formato: <tr><td>col1</td><td> ... </td></tr>
        """
        detalle = "".join(["<td>"+col+"</td>" for col in L])
        return "<tr>"+ detalle +"</tr>"

    def crearFichero(self, texto, path):
        pass


class Director:

    def __init__(self, builder):
        self.builder = builder

    def convertirFichero(self, path, sep=";"):
        f = None
        nombre = path.partition(".")[0]
        cabs = True
        tabla = ""
        try:
            f = open(path)
            for linea in f:
                linea = linea.rstrip()
                L = linea.split(sep)
                if cabs:
                    tabla += self.builder.createCab(L)
                    cabs = False                    
                else:
                    tabla += self.builder.createDetalle(L)
            print(tabla)
                
        except Exception as e:
            print(e)

        finally:
            if f:
                f.close()


if __name__ == "__main__":

    builder = BuilderHTML()
    director = Director(builder)
    director.convertirFichero("Empleados.txt")
