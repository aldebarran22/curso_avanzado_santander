"""
Ficheros names de EEUU
"""

import pandas as pd
from functools import reduce

path = (
    "D:/OneDrive/Escritorio/python_avanzado_santander/practicas/avanzado2/pandas/names/"
)


def cargarAño(año):
    fichero = f"yob{año}.txt"
    cols = ["nombre", "sexo", "cuenta"]
    df = pd.read_csv(path + fichero, header=None, names=cols)
    df.set_index(["nombre", "sexo"], inplace=True)
    return df


def sumarDosAños(año1, año2):
    # No rellena datos faltantes con 0, muestra NaN
    df1 = cargarAño(año1)
    df2 = cargarAño(año2)
    resul = df1 + df2
    print(resul.head(10))


def sumarDosAñosOK(año1, año2):
    df1 = cargarAño(año1)
    df2 = cargarAño(año2)
    resul = df1.add(df2, fill_value=0)
    resul.sort_values(by="cuenta", ascending=False, inplace=True)
    return resul


def exportarHTML(df):
    # Resetear indices:
    df.reset_index(inplace=True)
    # print(df.head(10))
    df.to_html("../ficheros/pedidos.html", index=False)


def sumarRangoAños(ini, fin):
    # Sumar el rango de años y obtener el top ten:

    def sumarDF(df1, df2):
        resul = df1.add(df2, fill_value=0)
        return resul

    L = [cargarAño(y) for y in range(ini, fin + 1)]
    dfTotal = reduce(sumarDF, L)
    dfTotal.sort_values(by="cuenta", ascending=False, inplace=True)
    dfTotal.reset_index(inplace=True)
    resul = dfTotal.loc[:10]
    return resul


def concatenarRangoAños(ini, fin):
    # Concatena el rango de años y exportar:
    # inplace=False devuelve una copia del df y se carga en la lista L
    L = [cargarAño(y).reset_index(inplace=False) for y in range(ini, fin + 1)]
    dfTotal = pd.concat(L, ignore_index=True)
    dfTotal.sort_values(by=["sexo", "cuenta"], ascending=False, inplace=True)
    dfTotal.to_csv("../ficheros/concatenar.csv", sep=";")


"""
def suma(n1, n2):
    print(n1, n2)
    return n1+n2
L = [3,5,6,6,4,3,1,2,3]
print(reduce(suma, L))
exit()
"""

if __name__ == "__main__":
    # df = cargarAño(2007)
    # print(df.head(10))
    # print(df.loc['Madison','F'])

    # df = sumarDosAñosOK(2007, 2008)
    # exportarHTML(df)

    # df = sumarRangoAños(2000, 2005)
    # print(df)

    concatenarRangoAños(2000, 2005)
