"""
Generar ficheros en json y XML (dom)
Parsear documentos XML (SAX)
Búsquedas en documentos XML (Xpath)
"""

from base_datos import Empleado, Producto, Categoria
from base_datos import BaseDatos, path
import json
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.etree import ElementTree as ET


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
            producto.set("id", str(prod.id))

            nombre = SubElement(producto, "nombre")
            nombre.text = prod.nombre

            precio = SubElement(producto, "precio")
            precio.text = str(prod.precio)

            categoria = SubElement(producto, "categoria")
            nombreCat = SubElement(categoria, "nombre")
            nombreCat.text = prod.cat.nombre
            categoria.set("idcat", str(prod.cat.id))

            existencias = SubElement(producto, "existencias")
            existencias.text = str(prod.exis)

        # print(tostring(top))
        tree = ET.ElementTree()
        tree._setroot(top)
        tree.write(pathFich)

    except Exception as e:
        print(e)
    finally:
        if fich:
            fich.close()

def getNombreProductos(pathFich):
    with open(pathFich, "rt"):
        tree = ET.parse(pathFich)
    root = tree.getroot()
    print(tostring(root))


if __name__ == "__main__":
    bd = BaseDatos(path)
    L = bd.select()
    exportarJSON(L, "../ficheros/productos.json")

    L2 = importarJSON("../ficheros/productos.json")
    print(L2[:3])

    L = bd.select()
    exportarXML(L, "../ficheros/productos.xml")

    getNombreProductos("../ficheros/productos.xml")
