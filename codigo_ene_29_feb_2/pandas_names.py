"""
1) Operar con dos DataFrames
2) Obtener el TOP 5 de los nombres más utilizados (F y M)
en un rango de años.
"""
import pandas as pd
from pandas import DataFrame


def cargarDF(año):
    """Carga y devuelve un DataFrame"""
    path = f"../../practicas/avanzado2/pandas/names/yob{año}.txt"
    df = pd.read_csv(path, header=None, names=["nombre", "sexo", "cuenta"])
    df.set_index(["nombre", "sexo"], inplace=True)
    return df


def sumarDosAños(año1, año2):
    """Suma dos DataFrames con el operador +"""
    df1 = cargarDF(año1)
    df2 = cargarDF(año2)
    suma = df1 + df2
    return suma


def sumarDosAñosAdd(año1, año2, delindex=False):
    """Suma dos DataFrames con el método  add"""
    df1 = cargarDF(año1)
    df2 = cargarDF(año2)
    suma = df1.add(df2, fill_value=0)
    suma.sort_values("cuenta", inplace=True, ascending=False)
    if delindex:
        suma.reset_index(["nombre", "sexo"], inplace=True)
    return suma


if __name__ == "__main__":
    # df = cargarDF(1970)
    # print(df.head(5))

    dfSuma = sumarDosAñosAdd(1970, 1971)
    print(dfSuma.head(6))
