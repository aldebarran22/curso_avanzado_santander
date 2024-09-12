"""
Serializar un objeto producto extraido previamente
de la base de datos
"""

import pickle as p
from base_datos import BaseDatos, Producto, path

def cargarProducto(id):
    try:
        bd = BaseDatos(path)
        producto = bd.read(id)
        return producto

    except Exception as e:
        print(e.__class__.__name__, e)

