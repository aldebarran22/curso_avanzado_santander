"""
Generar ficheros de json con la librería json
"""
import json
from base_datos import Categoria, Producto, path, BaseDatos

def extraerProductos():
    try:
        bd = BaseDatos(path)
        productos = bd.select()
        print(productos[:3])

    except  Exception as e:
        print(e)

if __name__ == '__main__':
    extraerProductos()