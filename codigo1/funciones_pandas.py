"""
Operaciones con pandas
"""

import pandas as pd

def separarPaises(pathOrigen, carpetaDestino):
    """Genera un fichero excel por cada pais"""
    dfPedidos = pd.read_csv(pathOrigen, sep=';')
    paises = dfPedidos.pais.unique()
    for pais in paises:
        pathDestino = carpetaDestino+f'/{pais}.xlsx'
        print(f'Generando fichero: {pathDestino}')
        dfPedidos[dfPedidos.pais == pais].to_excel(pathDestino, index=False)


def sumarNombres(año1, año2):

    def cargaAño(año):
        path = f"../ficheros_curso/names/yob{año}.txt"
        df = pd.read_csv(path, header=None, names=['nombre','sexo','total'])
        return df
    
    # Código de sumarNombres:
    df1 = cargaAño(año1)
    df2 = cargaAño(año2)
    suma = df1 + df2
    print(suma.head())


if __name__ == '__main__':
    #separarPaises('../ficheros_curso/merge/Pedidos.txt', '../ficheros/paises')
    sumarNombres(2015, 2016)