"""
Librerías de Serialización en python: pickle y shelve
"""
import pickle as p
from base_datos import BaseDatos


def serializarPickle(L, path):
    pass


def deserializarPickle(path):
    pass


if __name__ == "__main__":
    bd = BaseDatos("../BBDD/empresa3.db")
    L = bd.selectEmpleados()
    print(L)

    serializarPickle(L, "empleados.bin")
    L2 = deserializarPickle("empleados.bin")
    print(L2)
