"""
Ficheros names de EEUU
"""

import pandas as pd

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
    df.to_html("../ficheros/pedidos.html", index=True)


if __name__ == "__main__":
    # df = cargarAño(2007)
    # print(df.head(10))
    # print(df.loc['Madison','F'])
    df = sumarDosAñosOK(2007, 2008)
    exportarHTML(df)
