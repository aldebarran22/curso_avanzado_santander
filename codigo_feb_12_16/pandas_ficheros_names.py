"""
Operaciones con los ficheros de los nombres de EEUU
"""

import pandas as pd
from pandas import DataFrame
from os.path import isfile
from functools import reduce

path = "../../practicas/avanzado2/pandas/names/"


def cargaAño(año):
    pathFile = path + f"yob{año}.txt"
    df = pd.read_csv(pathFile, header=None, names=["nombre", "sexo", "cuenta"])
    df.set_index(["nombre", "sexo"], inplace=True)
    # print(df.head())
    # print(df.loc['Mary','F']) Número de veces que se repite Mary en F
    return df


def sumarDosAnyos(año1, año2):
    df = cargaAño(año1)
    df2 = cargaAño(año2)
    # r = df + df2 Arrastra NaN si no existe el índice en uno de los dos fich.
    r = df.add(df2, fill_value=0)
    r.sort_values(by="cuenta", ascending=False, inplace=True)
    return r


def sumarDosDFs(año1, año2):
    # print(año1.head(3))
    # print(año2.head(3))
    # print("-" * 20)
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
    resul = reduce(sumarDosDFs, L)
    resul.reset_index(inplace=True)
    resul.to_json("ficheros/names.json", orient="records", indent=4)
    print(resul.head())
    # Obtener 3 filas de DF:
    print("-" * 10)
    print(resul.loc[:3])
    print("-" * 10)
    print(resul.iat[1, 0])  # Fila 1, col 0 (no cuentan los índices)


if __name__ == "__main__":
    r = sumarDosAnyos(1913, 1914)
    sumarAños(2012, 2020)

    # iterar por las filas:
    r.reset_index(inplace=True)
    i = 3
    # iterrows devuelve una tuplas (indice, serie)
    for t, serie in r.iterrows():
        i -= 1
        print(t, serie.values)
        print("-" * 10)
        if i == 0:
            break
