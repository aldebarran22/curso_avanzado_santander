"""
Limpiar un fichero con datos de un huracán y estudiar la  
correlación entre el viento y la presión
"""

import pandas as pd
import numpy as np

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
    # Versión < 2.0
    """
    df["DateTime"] = pd.to_datetime(
        "2005 " + df.Date + " " + df.Time.str.replace(" GMT", ""),
        infer_datetime_format=True,
    )
    """
    # Versión >= 2
    df["DateTime"] = pd.to_datetime(
        "2005 " + df.Date + " " + df.Time.str.replace(" GMT", ""),
        format="%Y %b %d %H:%M",
    )

    # df.info()
    df.drop(columns=["Date", "Time"], inplace=True)
    print(df.head())

    # Calcular la correlación entre el viento y la presión: con numpy
    t = np.corrcoef(df.Wind, df.Pressure)
    print("Correlación:", round(t[1][0] * 100, 2), "%")

    # Utilizando el objeto Series:
    print("Correlación:", round(df.Wind.corr(df.Pressure) * 100, 2), "%")

    df.info()

    # Devuelve un DF con las cols de tipo numérico:
    df2 = df.select_dtypes(include=["int16", "float32"])
    print(df2.head())
    print(df2.corr())  # Cruza todas las cols del DF


if __name__ == "__main__":
    limpiarDF(path + "IRMA.csv")
