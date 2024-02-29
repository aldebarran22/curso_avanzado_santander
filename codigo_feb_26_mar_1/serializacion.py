"""
Serialización con pickle, shelve y
pandas (read_pickle, to_pickle)
"""

import pandas as pd
from pandas import DataFrame
import pickle
import shelve
from fecha_hora import DateTime, Date, Time


def serializarDF(path_df, path_pickle):
    df = pd.read_csv(path_df, sep=";")
    df.to_pickle(path_pickle, protocol=5)


def deserializarDF(path_pickle):
    df = pd.read_pickle(path_pickle)
    print(df.head())


def serializar_pickle(path_df, path_pickle2):
    df = pd.read_csv(path_df, sep=";")
    fich = open(path_pickle2,"wb")
    pickle.dump(df, fich)
    fich.close()


if __name__ == "__main__":
    path_df = "../../practicas/avanzado2/pandas/merge/Pedidos.txt"
    path_pickle = "../ficheros/pedidos.bin"
    path_pickle2 = "../ficheros/pedidos2.bin"
    serializarDF(path_df, path_pickle)
    deserializarDF(path_pickle)
