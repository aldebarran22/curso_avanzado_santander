"""
Obtener información de la Base de datos en json / xml
"""

import json
from base_datos import Categoria, Producto, BaseDatos
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.etree import ElementTree


def exportarXML(path, pathDestino):
    try:
        bd = BaseDatos(path)
        L = bd.select()

        # Crear el elemento raíz del XML:
        top = Element("productos")
        for p in L:
            # Se crea una etiqueta por cada producto:
            producto = SubElement(top, "producto")

        print(tostring(top))

    except Exception as e:
        print(e)


def importarJSON(path):
    fich = None
    try:
        with open(path, "r", encoding="utf8") as fich:
            Ljson = json.load(fich)

            for d in Ljson:
                print(d["nombre"])

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
    exportarXML(path, "productos.xml")
