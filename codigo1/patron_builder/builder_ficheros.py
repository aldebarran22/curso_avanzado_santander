"""
Implementar un patrón builder para convertir un fichero CSV
a distintos formatos: XML, HTML, JSON
"""

import abc


class Builder(abc.ABC):

    @abc.abstractmethod
    def crearCabecera(self, L):
        pass

    @abc.abstractmethod
    def crearDetalle(self, L, **kwargs):
        pass


class BuilderHTML(Builder):

    def crearCabecera(self, L):
        cabecera = "".join([f"<th>{col}</th>" for col in L])
        return "<tr>" + cabecera + "</tr>"

    def crearDetalle(self, L, **kwargs):
        detalle = "".join([f"<td>{col}</td>" for col in L])
        return "<tr>" + detalle + "</tr>"


class BuilderJSON(Builder):
    
    def __init__(self):
        self.cabeceras = None
        self.lista = []

    def crearCabecera(self, L):
        self.cabeceras = L
        return ""
    
    def crearDetalle(self, L, **kwargs):
        dicc = dict(zip(self.cabeceras, L))
        self.lista.append(dicc)
        return ""


class BuilderXML(Builder):

    def __init__(self):
        self.cabeceras = None

    def crearCabecera(self, L):
        self.cabeceras = L
        return ""

    def crearDetalle(self, L, **kwargs):
        detalle = ""
        etiqueta = kwargs['etiqueta']
        for i, col in enumerate(L):
            cab = self.cabeceras[i]
            detalle += f"<{cab}>{col}</{cab}>"
        return f"<{etiqueta}>{detalle}</{etiqueta}>"


class Director:

    def __init__(self, builder):
        self.builder = builder
        self.nombreFichero = ""
        self.etiqueta = ""

    def __extraerEtiqueta(self, path):
        L = path.split("/")
        fichero = L[-1]
        t = fichero.partition('.')
        self.nombreFichero = t[0]
        self.etiqueta = t[0][:-1].lower()

    def __getPath(self, path):
        return path.rpartition('.')[0]

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
                    tabla += self.builder.crearCabecera(L)
                    cabs = False
                else:
                    tabla += self.builder.crearDetalle(L, etiqueta=self.etiqueta)

            self.builder.crearFichero(tabla, self.__getPath(path))

        except Exception as e:
            raise e
        finally:
            if fich:
                fich.close()


if __name__ == "__main__":
    #builder = BuilderXML()
    builder = BuilderHTML()
    #builder = BuilderJSON()
    director = Director(builder)
    director.convertirFormato("Empleados.txt")
