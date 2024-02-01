"""
Cargar un dataframe y limpiar las columnas.
Convertir tipos de datos.
"""
import pandas as pd
import numpy as np
from pandas import DataFrame


def cargaDF(path):
    df = pd.read_csv(path, sep=";")
    df.columns = [col.strip() for col in df.columns]
    print(df.columns)

    # Latitud y longitud se convierten a float:
    df["Lat"] = pd.to_numeric(df.Lat.str[:-1], downcast="float")
    df["Lon"] = pd.to_numeric(df.Lon.str[:-1], downcast="float")

    # Viento y presión a integer:
    df["Wind"] = pd.to_numeric(df.Wind.str.replace(" mph", ""), downcast="integer")
    df["Pressure"] = pd.to_numeric(
        df.Pressure.str.replace(" mb", ""), downcast="integer"
    )

    df["DateTime"] = pd.to_datetime(
        "2005 " + df.Date + " " + df.Time.str.replace(" GMT", ""),
        infer_datetime_format=True,
    )

    df.drop(columns=["Date", "Time"], inplace=True)
    # df.info()
    return df


if __name__ == "__main__":
    df = cargaDF("../../practicas/avanzado2/pandas/csv/IRMA.csv")

    # Calcular la correlación entre la presión y la temperatura:
    correlacion = np.corrcoef(df.Pressure, df.Wind)
    valor = round(correlacion[0][1] * 100.0, 2)
    print("Correlación : ", valor, '%')
