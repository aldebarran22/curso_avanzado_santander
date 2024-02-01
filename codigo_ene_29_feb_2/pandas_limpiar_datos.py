"""
Cargar un dataframe y limpiar las columnas.
Convertir tipos de datos.
"""
import pandas as pd
from pandas import DataFrame


def cargaDF(path):
    df = pd.read_csv(path, sep=";")
    df.columns = [col.strip() for col in df.columns]
    print(df.columns)

    # Latitud y longitud se convierten a float:
    df["Lat"] = pd.to_numeric(df.Lat.str[:-1], downcast="float")
    df["Lon"] = pd.to_numeric(df.Lon.str[:-1], downcast="float")

    # Viento y presión a integer:
    df["Wind"] = pd.to_numeric(df.Wind.str.replace(" mph",""), downcast="integer")
    df["Pressure"] = pd.to_numeric(df.Pressure.str.replace(" mb",""), downcast="integer")
    df.info()


if __name__ == "__main__":
    cargaDF("../../practicas/avanzado2/pandas/csv/IRMA.csv")
