"""
Generar ficheros en json y XML (dom)
Parsear documentos XML (SAX)
Búsquedas en documentos XML (Xpath)
"""

from base_datos import Empleado, Producto, Categoria
from base_datos import BaseDatos, path
import json
from xml.etree.ElementTree import iterparse, Element, SubElement, Comment, tostring
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
    # print(tostring(root))

    for nodo in root.findall(".//producto/nombre"):
        print(nodo.text)

    for nodo in root.findall(".//producto"):
        print(nodo.get("id"))


def getNombreProductosSAX(pathFich):
    # Devolver una lista de diccionarios con nombre y precio:
    eventos = ["start", "end"]
    L = []
    for evento, nodo in iterparse(pathFich, eventos):
        if evento == "start":

            if nodo.tag == "producto":
                d = dict()
                flag = True

            if nodo.tag == "nombre" and flag:
                d["nombre"] = nodo.text

            if nodo.tag == "precio":
                d["precio"] = float(nodo.text)

            if nodo.tag == "categoria":
                flag = False

        elif evento == "end":
            if nodo.tag == "producto":
                L.append(d)

    return L


if __name__ == "__main__":
    bd = BaseDatos(path)
    L = bd.select()
    exportarJSON(L, "../ficheros/productos.json")

    L2 = importarJSON("../ficheros/productos.json")
    print(L2[:3])

    L = bd.select()
    exportarXML(L, "../ficheros/productos.xml")

    getNombreProductos("../ficheros/productos.xml")
    R = getNombreProductosSAX("../ficheros/productos.xml")
    print(R[:3])
