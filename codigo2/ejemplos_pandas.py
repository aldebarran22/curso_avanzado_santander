import pandas as pd
from os import mkdir
from os.path import isdir
from functools import reduce

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


def cargarDFNames(año):
    path = f"../ficheros_curso/names/yob{año}.txt"
    df = pd.read_csv(path, header=None, names=['nombre','sexo','total'])
    df.set_index(["nombre","sexo"], inplace=True)
    return df

def sumarRangoAños(*años):  

    def sumarDF(df1, df2):
        suma = df1.add(df2, fill_value=0)
        suma.sort_values("total", ascending=False, inplace=True)
        return suma

    L = [cargarDFNames(año) for año in años]
    return reduce(sumarDF, L)


def sumarDosAños(año1, año2):
    """Suma dos años con el operador"""
    df1 = cargarDFNames(año1)
    df2 = cargarDFNames(año2)

    #suma = df1 + df2
    suma = df1.add(df2, fill_value=0)
    suma.sort_values("total", ascending=False, inplace=True)
    print(suma.head(6))
    print("---------------")
    print(suma.loc['Mallory','M']['total'])
    suma.reset_index(inplace=True)
    suma.to_html("../ficheros/names_2000_2001.html", index=False)

    
if __name__ == '__main__':
    #exportarPaises('../ficheros_curso/merge/Pedidos.txt', '../ficheros/paises')
    #cargarDFNames(2000)
    #sumarDosAños(2000, 2001)
    total = sumarRangoAños(2000, 2001, 2002)
    total.reset_index(inplace=True)
    total.to_json("../ficheros/names.json", indent=4, orient='records')
    #print(total.head(10))

    L = [cargarDFNames(año).reset_index() for año in [2000, 2001, 2002]]
    total2 = pd.concat(L, ignore_index=True)
    total2.sort_values(by="nombre", inplace=True, ascending=False)
    print(total2.head(10))
