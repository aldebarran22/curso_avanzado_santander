"""
Ficheros names de EEUU
"""

import pandas as pd

path = (
    "D:/OneDrive/Escritorio/python_avanzado_santander/practicas/avanzado2/pandas/names/"
)


def cargarAño(año):
    fichero = f"yob{año}.txt"
    df = pd.read_csv(path + fichero)
    return df


def sumarDosAños(año1, año2):
    df1 = cargarAño(año1)
    df2 = cargarAño(año2)
    resul = df1 + df2
    print(resul.head(10))


if __name__ == "__main__":
    df = cargarAño(2007)
    print(df.head(10))
    # sumarDosAños(2007, 2008)
