"""
Operaciones con los ficheros de los nombres de EEUU
"""

import pandas as pd
from os.path import isfile

path = "../../practicas/avanzado2/pandas/names/"


def cargaAño(año):
    pathFile = path + f"yob{año}.txt"
    df = pd.read_csv(pathFile, header=None, names=["nombre", "sexo", "cuenta"])
    df.set_index(["nombre", "sexo"], inplace=True)
    # print(df.head())
    # print(df.loc['Mary','F']) Número de veces que se repite Mary en F
    return df


def sumarDosAños(año1, año2):
    df = cargaAño(año1)
    df2 = cargaAño(año2)
    # r = df + df2 Arrastra NaN si no existe el índice en uno de los dos fich.
    r = df.add(df2, fill_value=0)
    r.sort_values(by="cuenta", ascending=False, inplace=True)
    return r

def sumarAños(ini, fin):
    for año in range(ini, fin+1):
        pathFile = path + f"yob{año}.txt"
        if isfile(pathFile):
            print('existe: ',pathFile)    
        else:
            print('no existe: ',pathFile)



if __name__ == "__main__":
    r = sumarDosAños(1913, 1914)
    sumarAños(2012, 2020)