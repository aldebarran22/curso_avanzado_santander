"""
Serializar un objeto producto extraido previamente
de la base de datos
"""

import shelve as s
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

def serializarShelve(pathFile, *productos):
    Shelf = s.open(pathFile)
    k = 1
    for prod in productos:
        clave = f"K-{k}"
        Shelf[clave] = prod
        k += 1
    Shelf.close()

if __name__ == '__main__':
    prod = cargarProducto(1)
    serializar("producto.dat", prod)
    prod2 = deserializar("producto.dat")
    print(prod)
    print(prod2)

    L = [cargarProducto(p) for p in [1,3,12,35,6]]
    serializarShelve("productos_shelve", *L)
    
    