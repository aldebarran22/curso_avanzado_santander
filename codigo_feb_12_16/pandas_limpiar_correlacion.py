"""
Limpiar un fichero CSV y estudiar la correlación
entre dos columnas: Viento y la Presión
"""

import pandas as pd
import numpy as np


def limpiarDF(path):
    df = pd.read_csv(path, delimiter=";")
    df.columns = [col.rstrip() for col in df.columns]
    df["Lat"] = pd.to_numeric(df.Lat.str[:-1], downcast="float")
    df["Lon"] = pd.to_numeric(df.Lon.str[:-1], downcast="float")
    df["Wind"] = pd.to_numeric(df.Wind.str.replace(" mph", ""), downcast="integer")
    df["Pressure"] = pd.to_numeric(
        df.Pressure.str.replace(" mb", ""), downcast="integer"
    )
    """
    df["DateTime"] = pd.to_datetime(
        "2005 " + df.Date + " " + df.Time.str.replace(" GMT", ""),
        infer_datetime_format=True,
    )
    """
    df["DateTime"] = pd.to_datetime(
        "2005 " + df.Date + " " + df.Time.str.replace(" GMT", ""),
        format="%Y %b %d %H:%M",
    )
    df.drop(columns=["Date", "Time"], inplace=True)
    df.info()
    print(df.head())

    # Correlación entre el viento y la presión:
    t = np.corrcoef(df.Wind, df.Pressure)
    print('Correlación:',t[0][1] * 100,'%')


if __name__ == "__main__":
    limpiarDF("pandas_ficheros/IRMA.csv")
