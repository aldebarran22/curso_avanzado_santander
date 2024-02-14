"""
Operaciones con los ficheros de los nombres de EEUU
"""

import pandas as pd

path = "../../practicas/avanzado2/pandas/names/"


def cargaAño(año):
    pathFile = path + f"yob{año}.txt"
    df = pd.read_csv(pathFile, header=None, names=["nombre", "sexo", "cuenta"])
    df.set_index(["nombre", "sexo"], inplace=True)
    # print(df.head())
    # print(df.loc['Mary','F']) Número de veces que se repite Mary en F
    return df


if __name__ == "__main__":
    df = cargaAño(1914)
    df2 = cargaAño(1913)
    # r = df + df2
    # print(r.head(10))
