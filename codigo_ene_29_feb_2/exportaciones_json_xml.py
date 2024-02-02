"""
Obtener información de la Base de datos en json / xml
"""

import json
from base_datos import Categoria, Producto, BaseDatos


def exportarXML():
    pass


def exportarJSON():
    pass


def testBD(path, pathDestino):
    fich = None
    try:
        #fich = open(pathDestino, "w")
        bd = BaseDatos(path)
        L = bd.select()
        Ljson = [producto.to_json() for producto in L]

        with open(pathDestino, 'w', encoding='utf8') as fich:
            json.dump(Ljson, fich, ensure_ascii=False)       

    except Exception as e:
        print(e)
    finally:
        if fich:
            fich.close()


if __name__ == "__main__":
    path = "../../BBDD/empresa3.db"
    testBD(path, "productos.json")
