"""
Con la libreria de pandas generar un fichero
por cada pedido.
"""

import pandas as pd

def exportarPaises(path):
    dt = pd.read_csv(path, sep=";")
    paises = sorted(dt.pais.unique())
    for p in paises:
        path_pais = f"../ficheros/pedidos/{p}.csv"
        dt[dt.pais==p].to_csv(path_pais, index=False, decimal=",", sep=";")

if __name__ == '__main__':
    exportarPaises('../ficheros_curso/merge/Pedidos.txt')
