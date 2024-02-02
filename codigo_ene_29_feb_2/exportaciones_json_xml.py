"""
Obtener información de la Base de datos en json / xml
"""

import json
from base_datos import Categoria, Producto, BaseDatos


def exportarXML():
    pass


def importarJSON(path):
    fich = None
    try:
        with open(path, "r", encoding="utf8") as fich:
            Ljson = json.load(fich)
            print(Ljson[:2])

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
    exportarJSON(path, "productos.json")
    importarJSON("productos.json")
