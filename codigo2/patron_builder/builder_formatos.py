"""
Implementación del patrón Builder para convertir el formato
de un fichero CSV a:
- Json -> BuilderJSON
- XML -> BuilderXML
- HTML -> BuilderHTML
"""

import abc
import json

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

class BuilderXML(Builder):

    def __init__(self):
        self.cabeceras = ""
    
    def generarCabecera(self, L):
        self.cabeceras = L
        return ""
    
    def generarDetalle(self, L):
        detalle = ""
        for pos, dato in enumerate(L):
            detalle += f"<{self.cabeceras[pos]}>{dato}</{self.cabeceras[pos]}>"
        return detalle

   
    def grabarFichero(self, tabla, path):
        pass

class BuilderJSON(Builder):
    
    def __init__(self):
        self.cabeceras = ""
        self.lista = []
    
    def generarCabecera(self, L):
        self.cabeceras = L
        return ""
    
    def generarDetalle(self, L):
        dicc = dict(zip(self.cabeceras, L))
        self.lista.append(dicc)
        return ""

   
    def grabarFichero(self, tabla, path):
        pass

class Director:

    def __init__(self, builder, pathDestino):
        self.builder = builder
        self.tabla = ""
        self.pathDestino = pathDestino

    def __construirPath(self, pathOrigen):
        L = pathOrigen.split("/")
        fichero = L[-1]
        return self.pathDestino + "/" + fichero.partition('.')[0]

    def build(self, pathOrigen, sep=';'):
        fich = None
        cabs = True
        pathFichero = self.__construirPath(pathOrigen) 
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

            self.builder.grabarFichero(self.tabla, )

        except Exception as e:
            raise e
        finally:
            if fich:
                fich.close()


if __name__ == '__main__':
    try:
        builder = BuilderJSON()
        director = Director(builder, "destino")
        director.build("origen/Empleados.txt")
    except Exception as e:
        print(e)
