"""
Generar ficheros de json con la librería json
"""

import json
from base_datos import Categoria, Producto, path, BaseDatos


def extraerProductos():
    fich = None
    try:
        bd = BaseDatos(path)
        fich = open("productos.json", "w")
        productos = bd.select()
        L = [p.to_json() for p in productos]
        print("Fichero json generado")
        json.dump(L, fich, indent=4)

    except Exception as e:
        print(e)

    finally:
        if fich:
            fich.close()


if __name__ == "__main__":
    extraerProductos()
