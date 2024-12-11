"""
Implementar un patrón builder para convertir un fichero CSV
a distintos formatos: XML, HTML, JSON
"""

import abc
import json


class Builder(abc.ABC):

    @abc.abstractmethod
    def crearCabecera(self, L, **kwargs):
        pass

    @abc.abstractmethod
    def crearDetalle(self, L):
        pass

    @abc.abstractmethod
    def crearFichero(self, tabla, path):
        pass


class BuilderHTML(Builder):

    def crearCabecera(self, L, **kwargs):
        cabecera = "".join([f"<th>{col}</th>" for col in L])
        return "<tr>" + cabecera + "</tr>"

    def crearDetalle(self, L):
        detalle = "".join([f"<td>{col}</td>" for col in L])
        return "<tr>" + detalle + "</tr>"

    def crearFichero(self, tabla, path):
        fich = None
        fichOut = None
        try:
            fich = open("plantilla.html", "r")
            html = fich.read()
            tabla = f"<table>{tabla}</table>"
            html = html.replace("<body></body>",f"<body>{tabla}</body>")
            fichOut = open(path+".html", "w")
            fichOut.write(html)

        except Exception as e:
            raise e
        
        finally:
            if fich:
                fich.close()

            if fichOut:
                fichOut.close()


class BuilderJSON(Builder):

    def __init__(self):
        self.cabeceras = None
        self.lista = []

    def crearCabecera(self, L, **kwargs):
        self.cabeceras = L
        return ""

    def crearDetalle(self, L):
        dicc = dict(zip(self.cabeceras, L))
        self.lista.append(dicc)
        return ""

    def crearFichero(self, tabla, path):
        fich = open(path + ".json", "w")
        json.dump(self.lista, fich, indent=4)
        fich.close()


class BuilderXML(Builder):

    def __init__(self):
        self.cabeceras = None
        self.etiqueta = ""
        self.nombreFichero = ""

    def crearCabecera(self, L, **kwargs):
        self.cabeceras = L
        self.etiqueta = kwargs["etiqueta"]
        self.nombreFichero = kwargs["nombreFichero"]
        return ""

    def crearDetalle(self, L):
        detalle = ""
        for i, col in enumerate(L):
            cab = self.cabeceras[i]
            detalle += f"<{cab}>{col}</{cab}>"
        return f"<{self.etiqueta}>{detalle}</{self.etiqueta}>"

    def crearFichero(self, tabla, path):
        xml = f"<{self.nombreFichero}>{tabla}</{self.nombreFichero}>"
        xml = "<?xml version='1.0' encoding='UTF-8'?>" + xml
        fich = open(path + ".xml", "w")
        fich.write(xml)
        fich.close()


class Director:

    def __init__(self, builder):
        self.builder = builder
        self.nombreFichero = ""
        self.etiqueta = ""

    def __extraerEtiqueta(self, path):
        L = path.split("/")
        fichero = L[-1]
        t = fichero.partition(".")
        self.nombreFichero = t[0].lower()
        self.etiqueta = t[0][:-1].lower()

    def __getPath(self, path):
        return path.rpartition(".")[0]

    def convertirFormato(self, path, sep=";"):
        """Va leyendo el fichero y convirtiendo el CSV al formato
        para ello utiliza el builder"""
        fich = None
        cabs = True
        tabla = ""
        try:
            self.__extraerEtiqueta(path)
            fich = open(path, "r")
            for linea in fich:
                linea = linea.rstrip()
                L = linea.split(sep)
                if cabs:
                    tabla += self.builder.crearCabecera(
                        L, etiqueta=self.etiqueta, nombreFichero=self.nombreFichero
                    )
                    cabs = False
                else:
                    tabla += self.builder.crearDetalle(L)

            self.builder.crearFichero(tabla, self.__getPath(path))

        except Exception as e:
            raise e
        finally:
            if fich:
                fich.close()


if __name__ == "__main__":
    # builder = BuilderXML()
    builder = BuilderHTML()
    # builder = BuilderJSON()
    director = Director(builder)
    director.convertirFormato("Pedidos.txt")
