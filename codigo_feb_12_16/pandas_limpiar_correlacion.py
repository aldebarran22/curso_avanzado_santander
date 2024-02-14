"""
Limpiar un fichero CSV y estudiar la correlación
entre dos columnas: Viento y la Presión
"""
import pandas as pd

def limpiarDF(path):
    df = pd.read_csv(path, delimiter=";")
    df.info()

if __name__ == "__main__":
    limpiarDF("pandas_ficheros/IRMA.csv")