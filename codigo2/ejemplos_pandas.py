import pandas as pd
from os import mkdir
from os.path import isdir

def exportarPaises(path, pathDestino):
    if not isdir(pathDestino):
        mkdir(pathDestino)
    
    # Cargar el fichero de pedidos:
    df = pd.read_csv(path, sep=';')
    paises = df.pais.unique()
    for pais in paises:
        pathPais = f"{pathDestino}/{pais}.xlsx"
        print('Generando el fichero: ' + pathPais)
        df[df.pais==pais].to_excel(pathPais, index=False)

        

if __name__ == '__main__':
    exportarPaises('../ficheros_curso/merge/Pedidos.txt', '../ficheros/paises')