"""
Obtener información de la Base de datos en json / xml
"""

import json
from base_datos import Categoria, Producto, BaseDatos
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.etree.ElementTree import iterparse
from xml.etree import ElementTree


def testXPath(path):
    with open(path, "rt") as f:
        tree = ElementTree.parse(f)
        # Capturar la etiqueta raíz
        root = tree.getroot()

        print('Nombre de los productos:')
        for t in root.findall(".//producto/nombre"):
            print(t.text)

        cat = set()
        for t in root.findall(".//producto/categoria/nombre"):
            cat.add(t.text)
            
        print(cat)


        


def importarXML(path):
    eventos = ["start", "end"]
    enCat = False
    L = []

    for evento, nodo in iterparse(path, eventos):
        # print(evento, nodo.tag)
        if evento == "start":
            if nodo.tag == "categoria":
                enCat = True

            if nodo.tag == "nombre" and not enCat:
                nombre = nodo.text

            if nodo.tag == "precio":
                precio = float(nodo.text)

        elif evento == "end":
            if nodo.tag == "categoria":
                enCat = False

            if nodo.tag == "producto":
                L.append((nombre, precio))
    print(L[:3])


def exportarXML(path, pathDestino):
    try:
        bd = BaseDatos(path)
        L = bd.select()

        # Crear el elemento raíz del XML:
        top = Element("productos")
        for p in L:
            # Se crea una etiqueta por cada producto:
            producto = SubElement(top, "producto")

            # Crear un att en cada producto con la PK
            producto.set("id", str(p.id))

            # Añadir las propiedades de cada producto
            nombre = SubElement(producto, "nombre")
            nombre.text = p.nombre

            # Otra etiqueta anidada:
            categoria = SubElement(producto, "categoria")
            categoria.set("idcat", str(p.cat.id))
            nombreCat = SubElement(categoria, "nombre")
            nombreCat.text = p.cat.nombre

            # Resto de propiedades de cada producto
            precio = SubElement(producto, "precio")
            precio.text = "%.2f" % p.precio

            existencias = SubElement(producto, "existencias")
            existencias.text = "%d" % p.exis

        print(tostring(top))

        # Grabar al fichero:
        tree = ElementTree.ElementTree()
        tree._setroot(top)
        tree.write(pathDestino)

    except Exception as e:
        print(e)


def procesarJSON(id=0, nombre="", cat=None, precio=0.0, exis=0):
    print(id, nombre)


def importarJSON(path):
    fich = None
    try:
        with open(path, "r", encoding="utf8") as fich:
            Ljson = json.load(fich)

            for d in Ljson:
                procesarJSON(**d)

    except Exception as e:
        print(e)
    finally:
        if fich:
            fich.close()


def exportarJSON(path, pathDestino):
    fich = None
    try:
        bd = BaseDatos(path)
        L = bd.select()
        Ljson = [producto.to_json() for producto in L]

        with open(pathDestino, "w", encoding="utf8") as fich:
            json.dump(Ljson, fich, ensure_ascii=False, indent=4)

    except Exception as e:
        print(e)
    finally:
        if fich:
            fich.close()


if __name__ == "__main__":
    path = "../../BBDD/empresa3.db"
    # exportarJSON(path, "productos.json")
    # importarJSON("productos.json")
    # exportarXML(path, "productos.xml")
    # importarXML("productos.xml")
    testXPath("productos.xml")
