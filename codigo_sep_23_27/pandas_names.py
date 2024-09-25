"""
Estudios sobre los nacimientos en EEUU
"""

import pandas as pd

def cargaDF(año):
    path = f"../ficheros_curso/names/yob{año}.txt"
    df = pd.read_csv(path, header=None, names=["nombre","sexo","total"])    
    df.set_index(["nombre","sexo"], inplace=True)
    return df

def sumarLista(año_ini, año_fin):
    # Cargar en una lista el rango de años.
    pass

def sumar(año1, año2):
    df1 = cargaDF(año1)
    df2 = cargaDF(año2)
    #suma = df1 + df2
    suma = df1.add(df2, fill_value=0)
    suma.sort_values("total", ascending=False, inplace=True)
    return suma

if __name__ == '__main__':
    suma = sumar(2016, 2015)
    print(suma.head())