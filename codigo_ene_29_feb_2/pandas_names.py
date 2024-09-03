"""
1) Operar con dos DataFrames
2) Obtener el TOP 5 de los nombres más utilizados (F y M)
en un rango de años.
"""
import pandas as pd
from pandas import DataFrame
from os import listdir


def ficheros():
    L = listdir("../../practicas/avanzado2/pandas/names")
    print(L)


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

def concatDosAños(año1, año2):
    """Copiar los dos ficheros en uno. Concatenar"""
    df1 = cargarDF(año1)
    df2 = cargarDF(año2)
    dfTodo = pd.concat([df1, df2])
    dfTodo.sort_values(by=['nombre','sexo'], inplace=True)
    return dfTodo


def sumarDosAñosAdd(año1, año2, sort=True, delindex=False):
    """Suma dos DataFrames con el método  add"""
    df1 = cargarDF(año1)
    df2 = cargarDF(año2)
    suma = df1.add(df2, fill_value=0)

    if sort:
        suma.sort_values("cuenta", inplace=True, ascending=False)

    if delindex:
        suma.reset_index(["nombre", "sexo"], inplace=True)
    return suma


def sumarRangoAños(ini, fin):
    dfSuma = cargarDF(ini)
    for año in range(ini + 1, fin + 1):
        dfAño = cargarDF(año)
        dfSuma = dfSuma.add(dfAño, fill_value=0)

    dfSuma.sort_values("cuenta", inplace=True, ascending=False)
    return dfSuma


if __name__ == "__main__":
    # df = cargarDF(1970)
    # print(df.head(5))

    dfTodo = concatDosAños(1970, 1971)
    print(dfTodo.head())
    print(dfTodo.shape)
  

    dfSuma = sumarDosAñosAdd(1970, 1971)
    print(dfSuma.head(6))
    print()
    dfSumaRango = sumarRangoAños(1970, 1975)
    print(dfSumaRango.head(6))

    # ficheros()
