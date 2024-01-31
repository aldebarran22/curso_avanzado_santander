"""
1) Operar con dos DataFrames
2) Obtener el TOP 5 de los nombres más utilizados (F y M)
en un rango de años.
"""
import pandas as pd
from pandas import DataFrame


def cargarDF(año):
    """Carga y devuelve un DataFrame"""
    path = f"../../practicas/avanzado2/pandas/names/{año}.txt"
    df = pd.read_csv(path)
    return df


def sumarDosAños(año1, año2):
    """Suma dos DataFrames con el operador +"""
    pass


if __name__ == "__main__":
    df = cargarDF(1970)
    print(df.head(5))
    # dfSuma = sumarDosAños(1970, 1971)
    # print(dfSuma.head(6))
