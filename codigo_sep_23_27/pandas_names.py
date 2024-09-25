"""
Estudios sobre los nacimientos en EEUU
"""

import pandas as pd

def cargaDF(año):
    path = f"../ficheros_curso/names/yob{año}.txt"
    df = pd.read_csv(path)
    return df

if __name__ == '__main__':
    df = cargaDF(2016)
    print(df.head())