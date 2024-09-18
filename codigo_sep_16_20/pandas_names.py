
import pandas as pd

def cargaDF(año):
    path = f"../ficheros/names/yob{año}.txt"
    return pd.read_csv(path)

def sumarAños(año1, año2):
    df1 = cargaDF(año1)
    df2 = cargaDF(año2)
    suma = df1 + df2
    return suma
    

if __name__ == '__main__':
    #suma = sumarAños(2000, 2001)
    #print(suma.head())
    df = cargaDF(2000)
    print(df.head())