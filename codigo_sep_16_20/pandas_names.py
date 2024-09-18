import pandas as pd
from functools import reduce


def cargaDF(año):
    path = f"../ficheros_curso/names/yob{año}.txt"
    print(path)
    df = pd.read_csv(path, header=None, names=["nombre", "sexo", "cuenta"])
    df.set_index(["nombre", "sexo"], inplace=True)
    return df


def sumarAños(año1, año2):
    df1 = cargaDF(año1)
    df2 = cargaDF(año2)
    # suma = df1 + df2
    suma = df1.add(df2, fill_value=0)
    suma.sort_values("cuenta", ascending=False, inplace=True)
    return suma


def sumarDF(df1, df2):
    return df1.add(df2, fill_value=0)


if __name__ == "__main__":
    # df = cargaDF(2000)
    # print(df.head())

    """
    suma = sumarAños(2000, 2001)
    # print(suma.head())
    print(suma.loc["Madison"])
    print(suma.loc["Madison", "F"]["cuenta"])
    suma.reset_index(inplace=True)
    print(suma.head())
    """

    # Sumar una lista con los dataframes
    """
    L = [cargaDF(y) for y in range(2000, 2006)]
    total = reduce(sumarDF, L)
    total.sort_values("cuenta", ascending=False, inplace=True)
    print(total.head(10))
    """

    # Concatenar y exportar la lista anterior:
    # reset_index lo hacemos con una copia.
    L = [cargaDF(y).reset_index() for y in range(2000, 2006)]
    todo = pd.concat(L, ignore_index=True)
    todo.sort_values("nombre", inplace=True)
    todo.to_html("../ficheros/names.html")
