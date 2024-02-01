"""
Librerías de Serialización en python: pickle y shelve
"""
import pickle as p
import shelve
from base_datos import BaseDatos

def serializarConShelve(path, *empleados):
    shelf = None
    try:
        shelf = shelve.open(path)
        k = 1
        for e in empleados:
            clave = f"k{k}"
            shelf[clave] = e
            k+=1
            
    except Exception as e:
        print(e)
    finally:
        if shelf: shelf.close()

def serializarPickle(L, path):
    fich = None
    try:
        fich = open(path, "wb")
        p.dump(L, fich, protocol=2)

    except Exception as e:
        print(e)
    finally:
        if fich:
            fich.close()


def deserializarPickle(path):
    fich = None
    try:
        fich = open(path, "rb")
        obj = p.load(fich)
        return obj

    except Exception as e:
        print(e)
    finally:
        if fich:
            fich.close()


if __name__ == "__main__":
    bd = BaseDatos("../BBDD/empresa3.db")
    L = bd.selectEmpleados()
    print(L)
    print("-" * 10)
    serializarPickle(L, "empleados.bin")
    L2 = deserializarPickle("empleados.bin")
    print(L2)
