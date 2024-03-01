"""
Generar ficheros en json y XML (dom)
Parsear documentos XML (SAX)
Búsquedas en documentos XML (Xpath)
"""

from base_datos import Empleado, Producto, Categoria
from base_datos import BaseDatos, path
import json
from xml.etree.ElementTree import Element, SubElement, Comment, tostring


def exportarJSON(L, pathFich):
    fich = None
    try:
        fich = open(pathFich, "w")
        Ljson = [obj.to_json() for obj in L]
        json.dump(Ljson, fich, indent=4)
    except Exception as e:
        print(e)
    finally:
        if fich:
            fich.close()


def importarJSON(pathFich):
    fich = None
    try:
        fich = open(pathFich, "r")
        Ljson = json.load(fich)
        L = [Producto.create(dicc) for dicc in Ljson]
        return L

    except Exception as e:
        print(e)
    finally:
        if fich:
            fich.close()


def exportarXML(L, pathFich):
    fich = None
    try:
        top = Element("productos")
        comment = Comment("productos de la bd")
        top.append(comment)

        for prod in L:
            producto = SubElement(top, "producto")

            nombre = SubElement(producto, "nombre")
            nombre.text = prod.nombre

            precio = SubElement(producto, "precio")
            precio.text = str(prod.precio)

        print(tostring(top))

    except Exception as e:
        print(e)
    finally:
        if fich:
            fich.close()


if __name__ == "__main__":
    bd = BaseDatos(path)
    L = bd.select()
    exportarJSON(L, "../ficheros/productos.json")

    L2 = importarJSON("../ficheros/productos.json")
    print(L2[:3])

    exportarXML(L, "../ficheros/productos.xml")
