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

def serializar(pathFile, producto):
    fich = None
    try:
        fich = open(pathFile, 'wb')
        p.dump(producto, fich)

    except Exception as e:
        print(e.__class__.__name__, e)

    finally:
        if fich: fich.close()

def deserializar(pathFile):
    fich = None
    try:
        fich = open(pathFile, 'rb')
        producto = p.load(fich)
        return producto

    except Exception as e:
        print(e.__class__.__name__, e)

    finally:
        if fich: fich.close()

if __name__ == '__main__':
    prod = cargarProducto(1)
    serializar("producto.dat", prod)
    prod2 = deserializar("producto.dat")
    print(prod)
    print(prod2)
    