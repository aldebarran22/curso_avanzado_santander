"""
Serializar objetos con:
pickle: 1 objeto por fichero
shelve: varios objetos por fichero (trata como un dict)
"""

import pickle as p
import shelve as s
from base_datos import Categoria, Producto, BaseDatos, path


def serializarPickle(path, objeto):
    fich = None
    try:
        fich = open(path, "wb")
        p.dump(objeto, fich)

    except Exception as e:
        print(e)
    finally:
        if fich:
            fich.close()


def deserializarPickle(path):
    fich = None
    try:
        fich = open(path, "rb")
        objeto = p.load(fich)
        return objeto
    except Exception as e:
        print(e)

    finally:
        if fich:
            fich.close()


def serializarShelve(path, *objetos):    
    try:
        Shelf = s.open(path)
        for pos, obj in enumerate(objetos):
            clave = f"K-{pos+1}"
            Shelf[clave] = obj
            
        Shelf.close()
    except Exception as e:
        print(e)
  
        


def deserializarShelve(path, key):
    fich = None
    try:
        pass
    except Exception as e:
        pass
    finally:
        if fich:
            fich.close()


if __name__ == "__main__":
    bd = BaseDatos(path)
    prod = bd.read(1)
    prod2 = bd.read(2)
    prod3 = bd.read(3)
    print(prod)
    serializarPickle("producto.bin", prod)
    prod_2 = deserializarPickle("producto.bin")
    print(prod_2)

    serializarShelve("productos", prod, prod2, prod3)
