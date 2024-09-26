"""
Serializar objetos con:
pickle: 1 objeto por fichero
shelve: varios objetos por fichero (trata como un dict)
"""

import pickle as p
import shelve as s


def serializarPickle(path, objeto):
    fich = None
    try:
        pass
    except Exception as e:
        pass
    finally:
        if fich:
            fich.close()


def deserializarPickle(path):
    fich = None
    try:
        pass
    except Exception as e:
        pass
    finally:
        if fich:
            fich.close()


def serializarShelve(path, *objeto):
    fich = None
    try:
        pass
    except Exception as e:
        pass
    finally:
        if fich:
            fich.close()


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
    pass
