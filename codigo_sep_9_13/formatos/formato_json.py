"""
Generar un fichero json a partir de la BD.
"""

import json
from base_datos import path, BaseDatos, Categoria, Producto


def exportarJson():   
    fich = None 
    try:
        bd = BaseDatos(path)
        fich = open("productos.json","w")
        categorias = bd.select()
        cat_json = [cat.to_json() for cat in categorias]
        #print(cat_json[:3])
        json.dump(cat_json, fich, indent=4)

    except Exception as e:
        print(e.__class__.__name__, e)

    finally:
        if fich: fich.close()


def importarJson():
    pass


if __name__ == "__main__":
    exportarJson()
