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

def serializarShelve(pathFile, *objetos):
    Shelf = shelve.open(pathFile)
    for pos, obj in enumerate(objetos):
        clave = f"CLAVE-{pos+1}"
        Shelf[clave] = obj
    Shelf.close()


if __name__ == '__main__':
    bd = BaseDatos(path)
    prod = bd.read(1)
    print(prod)
    serializarPickle("pickle_producto.bin", prod)
    prod2 = deserializarPickle("pickle_producto.bin")
    print(prod2)

    cat = bd.readCategoria(2)
    serializarShelve("serializar_shelve", cat, prod, ["item1","item2"])
    

