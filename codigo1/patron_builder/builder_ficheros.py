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
        cabecera = "".join([f"<th>{col}</th>" for col in L])
        return "<tr>" + cabecera + "</tr>"
   
    def crearDetalle(self,L):
        detalle = "".join([f"<td>{col}</td>" for col in L])
        return "<tr>" + detalle + "</tr>"

class BuilderJSON(Builder):
    pass

class BuilderXML(Builder):

    def __init__(self):
        self.cabeceras = None
    
    def crearCabecera(self,L):
        self.cabeceras = L
        return ""

    def crearDetalle(self,L):
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

            print(tabla)

        except Exception as e:
            raise e
        finally:
            if fich:
                fich.close()

if __name__ == '__main__':
    builder = BuilderHTML()
    director = Director(builder)
    director.convertirFormato("Pedidos.txt")


