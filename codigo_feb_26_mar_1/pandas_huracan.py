"""
Limpiar un fichero con datos de un huracán y estudiar la  
correlación entre el viento y la presión
"""

import pandas as pd

path = (
    "D:/OneDrive/Escritorio/python_avanzado_santander/practicas/avanzado2/pandas/csv/"
)


def limpiarDF(pathFich):
    df = pd.read_csv(pathFich, sep=";")
    df.columns = [col.rstrip() for col in df.columns]
    df["Lat"] = pd.to_numeric(df.Lat.str[:-1], downcast="float")
    df["Lon"] = pd.to_numeric(df.Lon.str[:-1], downcast="float")
    df["Wind"] = pd.to_numeric(df.Wind.str.replace(" mph", ""), downcast="integer")
    df["Pressure"] = pd.to_numeric(
        df.Pressure.str.replace(" mb", ""), downcast="integer"
    )
    df.info()


if __name__ == "__main__":
    limpiarDF(path + "IRMA.csv")
