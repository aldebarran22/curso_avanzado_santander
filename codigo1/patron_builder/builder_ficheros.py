"""
Implementar un patrón builder para convertir un fichero CSV
a distintos formatos: XML, HTML, JSON
"""

import abc

class Builder(abc.ABC):

    @abc.abstractmethod
    def crearCabecera(self,L):
        pass

    @abc.abstractmethod
    def crearDetalle(self,L):
        pass

class BuilderHTML(Builder):

    def crearCabecera(self,L):
        pass
   
    def crearDetalle(self,L):
        pass

class BuilderJSON(Builder):
    pass

class BuilderXML(Builder):
    pass

class Director:

    def __init__(self, builder):
        self.builder = builder

    def convertirFormato(self, path, sep=';'):
        """Va leyendo el fichero y convirtiendo el CSV al formato
        para ello utiliza el builder"""
        fich = None
        cabs = True
        tabla = ""
        try:
            fich = open(path, 'r')
            for linea in fich:
                linea = linea.rstrip()
                L = linea.split(sep)                
                if cabs:
                    tabla += self.builder.crearCabecera(L)
                    cabs = False
                else:
                    tabla += self.builder.crearDetalle(L)

        except Exception as e:
            raise e
        finally:
            if fich:
                fich.close()

if __name__ == '__main__':
    builder = BuilderHTML()
    director = Director(builder)
    director.convertirFormato("Empleados.txt")


