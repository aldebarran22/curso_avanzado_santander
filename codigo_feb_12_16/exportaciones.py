"""
Exportar a JSON / XML empleados de la BD
"""

from basedatosCRUD import BaseDatos, Empleado
import json, pickle, shelve
from xml.etree.ElementTree import iterparse, Element, SubElement, tostring, Comment
from xml.etree import ElementTree
from fecha_hora import Time, Date


def serializarShelve(path, *objetos):
    Shelf = shelve.open(path)
    n = len(objetos)
    i = 1
    for obj in objetos:
        clave = f"k-{i}"
        Shelf[clave] = obj
        i += 1
    Shelf.close()
    return n


def deserializarShelve(path, n):
    Shelf = shelve.open(path)
    for i in range(1, n + 1):
        clave = f"k-{i}"
        obj = Shelf[clave]
        i += 1
        print(obj)
    Shelf.close()


def serializarPickle(L, path):
    fich = None
    try:
        fich = open(path, "wb")
        pickle.dump(L, fich, protocol=2)
    except Exception as e:
        print(e)
    finally:
        if fich:
            fich.close()


def deserializarPickle(path):
    fich = None
    try:
        fich = open(path, "rb")
        L = pickle.load(fich)
        print(L)
        return L
    except Exception as e:
        print(e)
    finally:
        if fich:
            fich.close()


def exportarJSON(bd, path):
    fich = None
    try:
        fich = open(path, "w")
        empleados = bd.select()
        L = [emp.__dict__ for emp in empleados]
        json.dump(L, fich, indent=4)
        # print(json.dumps(L, indent=4)

    except Exception as e:
        print(e)
    finally:
        if fich:
            fich.close()


def importarJSON(path):
    fich = None
    try:
        fich = open(path, "r")
        # Restaurar una lista de dict de Python
        L = json.load(fich)
        # Pasar de la lista de dict a una lista de objetos Empleado
        empleados = [Empleado(**d) for d in L]
        return empleados

    except Exception as e:
        print(e)
    finally:
        if fich:
            fich.close()


def exportarXML(bd, path):
    top = Element("empleados")
    top.set("version", "1.0")
    empleados = bd.select()
    comentario = Comment("fichero de empleados de la BD")
    top.append(comentario)
    for e in empleados:
        empleado = SubElement(top, "empleado", {"id": str(e.id)})
        nombre = SubElement(empleado, "nombre")
        nombre.text = e.nombre
        cargo = SubElement(empleado, "cargo")
        cargo.text = e.cargo

    # Grabar en un fichero:
    tree = ElementTree.ElementTree()
    tree._setroot(top)
    tree.write(path)


def xpath(path):
    with open(path, "rt") as f:
        tree = ElementTree.parse(f)
    root = tree.getroot()
    # todos los nombres:
    L = [t.text for t in root.findall(".//nombre")]
    print(L[:6])

    # los nombres de las categorias: sin repetidos
    c = {t.text for t in root.findall(".//categoria/nombre")}
    print(c)


def importarXML(path):
    with open(path, "rt") as f:
        tree = ElementTree.parse(f)

    root = tree.getroot()
    # print(tostring(root))
    for nodo in root:
        print(nodo.tag, nodo.text, nodo.attrib)
        for n in nodo:
            print(n.tag, n.text)


def importarSAX(path):
    eventos = ["start", "end"]
    activo = True
    for evento, nodo in iterparse(path, eventos):

        if evento == "start":
            if nodo.tag == "nombre" and activo:
                nombre = nodo.text

            if nodo.tag == "categoria":
                activo = False

            if nodo.tag == "precio":
                precio = float(nodo.text)

        elif evento == "end":

            if nodo.tag == "categoria":
                activo = True

            if nodo.tag == "producto":
                print(nombre, precio)


if __name__ == "__main__":
    bd = BaseDatos("../BBDD/empresa3.db")
    # exportarJSON(bd, "ficheros/empleados.json")
    # L = importarJSON("ficheros/empleados.json")
    # print(L[:3])
    # exportarXML(bd, "ficheros/empleados.xml")
    # importarXML("ficheros/empleados.xml")
    # xpath("ficheros/productos.xml")
    # importarSAX("ficheros/productos.xml")
    serializarPickle(bd.select(), "ficheros/empleados.bin")
    L = deserializarPickle("ficheros/empleados.bin")

    n = serializarShelve(
        "ficheros/empleados", Time(9, 44, 55), Date(1, 1, 2020), bd.read(1)
    )
    deserializarShelve("ficheros/empleados", n)
