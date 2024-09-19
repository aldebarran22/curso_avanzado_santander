"""
Generar ficheros de json con la librería json
"""

import json
import pandas as pd
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
        productos = [Producto.create(d) for d in L]
        print(productos[:3])

    except Exception as e:
        print(e)

    finally:
        if fich:
            fich.close()

def cargarJsonDF(pathFile):
    df = pd.read_json(pathFile, orient="records")
    print(df.head())

def cargarJsonNormalizadoDF(pathFile):
    with open(pathFile, "r") as f:
        d = json.load(f)
        df = pd.json_normalize(d)   
        print(df.head())

if __name__ == "__main__":
    #extraerProductos("Bebidas")
    #cargarProductos("productos.json")
    cargarJsonDF("productos.json")
    cargarJsonNormalizadoDF("productos.json")