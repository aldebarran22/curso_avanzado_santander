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
    df["Lon"] = pd.to_numeric(df.Lon.str[:-1], downcast="float")
    df["Wind"] = pd.to_numeric(df.Wind.str.replace(" mph",""), downcast="integer")
    df["Pressure"] = pd.to_numeric(df.Pressure.str.replace(" mb",""), downcast="integer")
    # 2005 sep-16 15:00 GMT
    df["Datetime"] = pd.to_datetime(
        "2005 " + df.Date + " " + df.Time.str.replace(" GMT",""),
        format="%Y %b %d %H:%M"
    )
    df.drop(columns=["Date","Time"], inplace=True)
    df = df[["Datetime","Lat","Lon","Wind","Pressure"]]
    return df


if __name__ == '__main__':
    path = "../ficheros_curso/csv/MARIA.csv"
    df = cargaFichero(path)
    df.info()
    print(df.head())    