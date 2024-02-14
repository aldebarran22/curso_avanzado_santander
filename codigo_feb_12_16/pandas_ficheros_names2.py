"""
Operaciones con los ficheros de los nombres de EEUU
"""

import pandas as pd
from pandas import DataFrame
from os.path import isfile
from functools import reduce, singledispatch

path = "../../practicas/avanzado2/pandas/names/"


def cargaAño(año):
    pathFile = path + f"yob{año}.txt"
    df = pd.read_csv(pathFile, header=None, names=["nombre", "sexo", "cuenta"])
    df.set_index(["nombre", "sexo"], inplace=True)
    return df


@singledispatch
def sumarDosAnyos(año1, año2):
    print("función por defecto")


@sumarDosAnyos.register(int)
def _(año1, año2):
    df = cargaAño(año1)
    df2 = cargaAño(año2)
    return sumarDosAnyos(df, df2)


@sumarDosAnyos.register(DataFrame)
def _(año1, año2):
    r = año1.add(año2, fill_value=0)
    r.sort_values(by="cuenta", ascending=False, inplace=True)
    return r


def sumarAños(ini, fin):
    L = []
    for año in range(ini, fin + 1):
        pathFile = path + f"yob{año}.txt"
        if isfile(pathFile):
            L.append(cargaAño(año))
        else:
            print("no existe: ", pathFile)
    print("Se han cargado: ", len(L))
    resul = reduce(sumarDosAnyos, L)
    print(resul.head())


if __name__ == "__main__":
    r = sumarDosAnyos(1913, 1914)
    sumarAños(2012, 2020)

    sumarDosAnyos("a","b")
