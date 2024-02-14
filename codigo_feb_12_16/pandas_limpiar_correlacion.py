"""
Limpiar un fichero CSV y estudiar la correlación
entre dos columnas: Viento y la Presión
"""
import pandas as pd

def limpiarDF(path):
    df = pd.read_csv(path, delimiter=";")
    df.columns = [col.rstrip() for col in df.columns]
    df['Lat'] = pd.to_numeric(df.Lat.str[:-1], downcast="float")
    df['Lon'] = pd.to_numeric(df.Lon.str[:-1], downcast="float")
    df['Wind'] = pd.to_numeric(df.Wind.str.replace(" mph",""),downcast="integer")
    df.info()
    

if __name__ == "__main__":
    limpiarDF("pandas_ficheros/IRMA.csv")