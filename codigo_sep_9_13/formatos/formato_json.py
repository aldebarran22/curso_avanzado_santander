"""
Generar un fichero json a partir de la BD.
"""

import json
from base_datos import path, BaseDatos, Categoria, Producto


def exportarJson():    
    try:
        bd = BaseDatos(path)
        categoria = bd.select()
        print(categoria)

    except Exception as e:
        print(e.__class__.__name__, e)


def importarJson():
    pass


if __name__ == "__main__":
    exportarJson()
