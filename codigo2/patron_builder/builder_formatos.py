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
        cabeceras = ""
        for col in L:
            cabeceras += f"<th>{col}</th>"
        return f"<tr>{cabeceras}</tr>"

    
    def generarDetalle(self, L):
        detalle = "".join([f"<td>{campo}</td>" for campo in L])
        return f"<tr>{detalle}</tr>"

   
    def grabarFichero(self, tabla, path):
        pass

class Director:

    def __init__(self, builder):
        self.builder = builder
        self.tabla = ""

    def build(self, pathOrigen, sep=';'):
        fich = None
        cabs = True
        try:
            fich = open(pathOrigen, 'r')
            for fila in fich:
                fila = fila.rstrip()
                L = fila.split(sep)
                if cabs:
                    self.tabla += self.builder.generarCabecera(L)
                    cabs = False
                else:
                    self.tabla += self.builder.generarDetalle(L)

            print(self.tabla)

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
    try:
        builder = BuilderHTML()
        director = Director(builder)
        director.build("origen/Empleados.txt")
    except Exception as e:
        print(e)
