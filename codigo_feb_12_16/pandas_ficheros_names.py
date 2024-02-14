"""
Operaciones con los ficheros de los nombres de EEUU
"""
import pandas as pd

path = "../../practicas/avanzado2/pandas/names/"

def cargaAño(año):
    pathFile = path+f"yob{año}.txt"
    df = pd.read_csv(pathFile)
    print(df.head())
    return df

if __name__ == '__main__':
    df = cargaAño(1914)