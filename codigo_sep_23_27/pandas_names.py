"""
Estudios sobre los nacimientos en EEUU
"""

import pandas as pd
from functools import reduce

def cargaDF(año):
    path = f"../ficheros_curso/names/yob{año}.txt"
    df = pd.read_csv(path, header=None, names=["nombre","sexo","total"])    
    df.set_index(["nombre","sexo"], inplace=True)
    return df

def sumar(año1, año2):    
    df1 = cargaDF(año1)
    df2 = cargaDF(año2)
    #suma = df1 + df2
    suma = df1.add(df2, fill_value=0)
    suma.sort_values("total", ascending=False, inplace=True)
    return suma

def sumar2DF(df1, df2):
    suma = df1.add(df2, fill_value=0)
    suma.sort_values("total", ascending=False, inplace=True)
    return suma

def sumarLista(año_ini, año_fin):
    # Cargar en una lista el rango de años.    
    result = [cargaDF(year) for year in range(año_ini, año_fin+1)]    
    print([f.shape for f in result])
    todo = reduce(sumar2DF, result)
    print(todo.head())
    print(todo["total"]["Jacob","M"])
    print(todo.loc["Jacob","M"]["total"])

if __name__ == '__main__':
    #suma = sumar(2016, 2015)
    #print(suma.head())

    sumarLista(2000, 2005)