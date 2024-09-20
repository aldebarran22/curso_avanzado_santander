"""
Serialización de objetos con las librerías:
pickle y shelve.
"""

import pickle
import shelve

from base_datos import BaseDatos, path, Producto, Categoria

def serializarPickle(pathFile, objeto):
    fich = None
    try:
        fich = open(pathFile, "wb")
        pickle.dump(objeto, fich)
    except Exception as e:
        print(e)
    finally:
        if fich: fich.close()

def deserializarPickle(pathFile):
    fich = None
    try:
        fich = open(pathFile, "rb")
        objeto = pickle.load(fich)
        return objeto
    
    except Exception as e:
        print(e)
    finally:
        if fich: fich.close()

if __name__ == '__main__':
    bd = BaseDatos(path)
    prod = bd.read(1)
    print(prod)
    serializarPickle("pickle_producto.bin", prod)
    prod2 = deserializarPickle("pickle_producto.bin")
    print(prod2)
