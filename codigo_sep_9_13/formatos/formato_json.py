"""
Generar un fichero json a partir de la BD.
"""

import json
from base_datos import path, BaseDatos, Categoria, Producto


def exportarJson(pathFile, categoria=None):   
    fich = None 
    try:
        bd = BaseDatos(path)
        fich = open(pathFile,"w")
        categorias = bd.select(categoria)
        cat_json = [cat.to_json() for cat in categorias]
        #print(cat_json[:3])
        json.dump(cat_json, fich, indent=4)

    except Exception as e:
        print(e.__class__.__name__, e)

    finally:
        if fich: fich.close()


def importarJson(pathFile):
    fich = None 
    try:
        fich = open(pathFile, "r")
        categorias = json.load(fich)
        print(categorias[:3])

        # Conversión de diccionarios a objetos:
        objetos = [Producto.create(d) for d in categorias]
        print()
        print(objetos[:3])

    except Exception as e:
        print(e.__class__.__name__, e)

    finally:
        if fich: fich.close()


if __name__ == "__main__":
    #exportarJson("productos.json")
    importarJson("productos.json")