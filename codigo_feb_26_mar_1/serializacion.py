"""
Serialización con pickle, shelve y
pandas (read_pickle, to_pickle)
"""

import pandas as pd
from pandas import DataFrame
import pickle
import shelve
from fecha_hora import DateTime, Date, Time


def serializarShelve(path_shelve, *objetos):
    Shelf = shelve.open(path_shelve, protocol=5)
    n = 1
    for obj in objetos:
        clave = f"K-{n}"
        Shelf[clave] = obj
        n += 1
    Shelf.close()
    return n


def deserializarShelve(path_shelve, n):
    Shelf = shelve.open(path_shelve, protocol=5)
    print("k-2: ", Shelf.get("K-2"))
    print("k-1: ", Shelf["K-1"])
    print("k-3: ", Shelf["K-3"])
    print("Existe clave K-4: ", "K-4" in Shelf)
    Shelf.close()


def serializarDF(path_df, path_pickle):
    df = pd.read_csv(path_df, sep=";")
    df.to_pickle(path_pickle, protocol=5)


def deserializarDF(path_pickle):
    df = pd.read_pickle(path_pickle)
    print(df.head())


def serializar_pickle(path_df, path_pickle2):
    df = pd.read_csv(path_df, sep=";")
    fich = open(path_pickle2, "wb")
    pickle.dump(df, fich)
    fich.close()


def deserializar_pickle(path_pickle2):
    fich = open(path_pickle2, "rb")
    df = pickle.load(fich)
    print(df.head())
    fich.close()


if __name__ == "__main__":
    path_df = "../../practicas/avanzado2/pandas/merge/Pedidos.txt"
    path_pickle = "../ficheros/pedidos.bin"
    path_pickle2 = "../ficheros/pedidos2.bin"
    path_shelve = "../ficheros/pedidos3"
    serializarDF(path_df, path_pickle)
    deserializarDF(path_pickle)
    serializar_pickle(path_df, path_pickle2)
    deserializar_pickle(path_pickle2)
    n = serializarShelve(path_shelve, Date(1, 5, 2000), Time(13, 55, 3), DateTime())
    deserializarShelve(path_shelve, n)
