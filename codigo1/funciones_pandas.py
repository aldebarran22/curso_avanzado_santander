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


def cargaAño(año):
    path = f"../ficheros_curso/names/yob{año}.txt"
    df = pd.read_csv(path, header=None, names=['nombre','sexo','total'])
    df.set_index(['nombre','sexo'], inplace=True) 
    return df


def sumarDFs(df1, df2):
    suma = df1.add(df2, fill_value=0)
    suma.sort_values("total", ascending=False, inplace=True)
    return suma

def sumarNombres(año1, año2):    
    # Código de sumarNombres:
    df1 = cargaAño(año1)
    df2 = cargaAño(año2)
    suma = sumarDFs(df1, df2)
    return suma    
    #print(suma.loc['Madison','F'])


if __name__ == '__main__':
    #separarPaises('../ficheros_curso/merge/Pedidos.txt', '../ficheros/paises')
    suma = sumarNombres(2015, 2016)
    print('TOP 5 de los años: 2015 y 2016')
    print(suma.head())