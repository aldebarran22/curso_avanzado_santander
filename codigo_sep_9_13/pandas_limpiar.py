"""
Conversiones de tipos de datos en las columnas del
fichero.
"""

import pandas as pd


def cargaFichero(path):
    df = pd.read_csv(path, sep=";")
    # Quitar espacios de los nombres de las columnas
    df.columns = [col.strip() for col in df.columns]
    df["Lat"] = pd.to_numeric(df.Lat.str[:-1], downcast="float")
    return df


if __name__ == '__main__':
    path = "../ficheros_curso/csv/MARIA.csv"
    df = cargaFichero(path)
    df.info()
    print(df.head())
    print(df.Lat)