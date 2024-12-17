"""
Generar ficheros XML a partir de una colección de objetos de la BD
Serialización de objetos con: pickle, shelve
"""

from base_datos import Producto, Categoria, BaseDatos
from xml.etree.ElementTree import (
    iterparse,
    Element,
    SubElement,
    tostring,
    Comment,
    ElementTree,
)
from xml.etree import ElementTree as ET
import pickle as p
import shelve as s


def generarXML(L, path):

    # Generar el nodo raiz:
    raiz = Element("productos")
    raiz.set("version", "1.0")
    comentario = Comment("Productos extraidos de la base de datos Empresa3.db")

    # Añadir el comentario al nodo raiz:
    raiz.append(comentario)

    # Generar un producto por cada objeto de la colección:
    for p in L:
        nodoProducto = SubElement(raiz, "producto")
        nodoProducto.attrib["id"] = str(p.id)
        nodoNombre = SubElement(nodoProducto, "nombre")
        nodoNombre.text = p.nombre
        nodoPrecio = SubElement(nodoProducto, "precio")
        nodoPrecio.text = str(round(p.precio, 2))
        nodoCat = SubElement(nodoProducto, "categoria")
        nodoCat.attrib["idcat"] = str(p.cat.id)
        nodoCatNombre = SubElement(nodoCat, "nombre")
        nodoCatNombre.text = p.cat.nombre
        nodoExistencias = SubElement(nodoProducto, "existencias")
        nodoExistencias.text = str(p.exis)

    et = ElementTree()
    et._setroot(raiz)
    et.write(path)

    # Imprimir el árbol
    # print(tostring(raiz, encoding='unicode'))


def cargarBuscar(path):

    # Cargar el DOM:
    with open(path, "rt") as fichero:
        tree = ET.parse(fichero)

    # Recuperar el nodo raíz;
    raiz = tree.getroot()
    # print(tostring(raiz))

    # Los nombres de los productos con XPath:
    # cad = ".//nombre"
    # Los nombres de la categorias:
    cad = ".//categoria/nombre"
    nombres = set([nodo.text for nodo in raiz.findall(cad)])
    print(nombres)

    # Obtener los ids de las categorias:
    cad = ".//categoria[@idcat='1']"
    for nodo in raiz.findall(cad):
        print(tostring(nodo))


def parsearConSAX(path):
    eventos = ["start", "end"]
    categorias = set()
    existe = False

    for event, nodo in iterparse(path, eventos):
        if event == "start":
            if nodo.tag == "categoria":
                existe = True

            if nodo.tag == "nombre" and existe:
                categorias.add(nodo.text)

        if event == "end":
            if nodo.tag == "categoria":
                existe = False

    return sorted(categorias, key=lambda obj: obj.capitalize())


def serializarPickle(objeto, path):
    fich = None
    try:
        fich = open(path, "wb")
        p.dump(objeto, fich, protocol=5)
    except Exception as e:
        print(e)
    finally:
        if fich:
            fich.close()


def deserializarPickle(path):
    fich = None
    try:
        fich = open(path, "rb")
        objeto = p.load(fich)
        return objeto

    except Exception as e:
        print(e)
    finally:
        if fich:
            fich.close()


def serializarShelve(path, *objetos):
    Shelf = s.open(path)
    for pos, obj in enumerate(objetos):
        clave = f"K-{pos+1}"
        Shelf[clave] = obj
    Shelf.close()


if __name__ == "__main__":
    try:
        bd = BaseDatos("empresa3.db")
        L = bd.select()
        # generarXML(L, "productos.xml")
        # cargarBuscar("productos.xml")
        # cats = parsearConSAX("productos.xml")
        # print(cats)

        # Serialización con pickle:
        serializarPickle(L, "productos.bin")
        L2 = deserializarPickle("productos.bin")
        print(L2[:3])

        serializarShelve("objetos", *L[:3])

    except Exception as e:
        print(e)
