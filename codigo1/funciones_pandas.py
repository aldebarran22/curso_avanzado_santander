"""
Operaciones con pandas
"""

import pandas as pd

def separarPaises(pathOrigen, carpetaDestino):
    """Genera un fichero excel por cada pais"""
    dfPedidos = pd.read_csv(pathOrigen, sep=';')
    paises = dfPedidos.pais.unique()
    for pais in paises:
        pathDestino = carpetaDestino+f"/{pais}.xlsx"
        print(f'Generando fichero: {pathDestino}')
        dfPedidos[dfPedidos.pais == pais].to_excel(pathDestino, index=False)


if __name__ == '__main__':
    separarPaises('../ficheros_curso/merge/Pedidos.txt', '../ficheros/paises')
