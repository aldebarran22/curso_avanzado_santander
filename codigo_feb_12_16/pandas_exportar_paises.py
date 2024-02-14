"""
A partir del fichero: Pedidos.txt
Generar un fichero CSV para cada país y copiar 
los pedidos de cada pais
"""
import pandas as pd

def exportarPaises(pathPedidos):
    df = pd.read_csv(pathPedidos, delimiter=';')
    print(df.shape)
    paises = df.pais.unique()
    for pais in paises:
        pathPais = f"ficheros/{pais}.csv"
        print(pathPais)
        df[df.pais == pais].to_csv(pathPais, index=False, decimal=',',sep=";")


if __name__ == "__main__":
    exportarPaises("pandas_ficheros/Pedidos.txt")
