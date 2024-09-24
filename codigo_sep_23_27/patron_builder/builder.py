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
    
    def __cargarPlantilla(self, path):
        fich = None
        try:
            fich = open(path, 'r')
            html = fich.read()
            return html
        
        except Exception as e:
            raise e

        finally:
            if fich: fich.close()

   
    def crearFichero(self, texto, path):
        fich = None
        pathFile = path + ".html"
        tablaHTML = f"<table>{texto}</table>"
        html = self.__cargarPlantilla("template.html")
        html = html.replace("<body></body>", f"<body>{tablaHTML}</body>")
        try:
            fich = open(pathFile, 'w')
            fich.write(html)
        except Exception as e:
            raise e

        finally:
            if fich: fich.close() 
        
    
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
            linea += f"<{self.cabs[pos]}>{i}</{self.cabs[pos]}>"
        return f"<{self.etiqueta}>{linea}</{self.etiqueta}>"

    def crearFichero(self, texto, path):
        pathFile = path + ".xml"
        xml = f"<{self.etiqueta+'s'}>{texto}</{self.etiqueta+'s'}>"
        xml = "<?xml version='1.0' encoding='UTF-8' ?>" + xml
        try:
            fich = open(pathFile, 'w')
            fich.write(xml)
        except Exception as e:
            raise e
        finally:
            if fich: fich.close() 

class Director:
    """Define el proceso de creación del 
    producto final, para ello utiliza un builder."""

    def __init__(self, builder):
        self.builder = builder
        self.nombreFichero = ""
        self.nombre = ""

    def convertirFichero(self, path, sep=';'):
        f = None
        cabs = True
        tabla = ""
        self.nombreFichero = path.partition(".")[0]
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
            self.builder.crearFichero(tabla, self.nombreFichero)

        except Exception as e:
            print(e)
        finally:
            if f:f.close()


if __name__ == '__main__':
    # Seleccionar un builder según el formato destino
    builder = BuilderXML()
    director = Director(builder)
    director.convertirFichero("Pedidos.txt")

    # python builder.py -xml Pedidos.txt
    # python builder.py -html Pedidos.txt
