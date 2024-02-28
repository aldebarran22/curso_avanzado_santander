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
    df.info()

if __name__ == '__main__':
    limpiarDF(path+"IRMA.csv")