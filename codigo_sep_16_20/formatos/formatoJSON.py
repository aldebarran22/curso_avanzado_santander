"""
Generar ficheros de json con la librería json
"""

import json
from base_datos import Categoria, Producto, path, BaseDatos


def extraerProductos(cat=None):
    fich = None
    try:
        pathFile = "productos.json" if cat is None else f"productos_{cat}.json"
        bd = BaseDatos(path)
        fich = open(pathFile, "w")
        productos = bd.select(cat)
        L = [p.to_json() for p in productos]
        print("Fichero json generado")
        json.dump(L, fich, indent=4)

    except Exception as e:
        print(e)

    finally:
        if fich:
            fich.close()

def cargarProductos(pathFile):
    fich = None
    try:
        fich = open(pathFile, "r")
        L = json.load(fich)
        print(L[:3])
        
    except Exception as e:
        print(e)

    finally:
        if fich:
            fich.close()

if __name__ == "__main__":
    #extraerProductos("Bebidas")
    cargarProductos("productos.json")
