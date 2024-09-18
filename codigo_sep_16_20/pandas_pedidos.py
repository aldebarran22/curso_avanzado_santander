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
        dt[dt.pais == p].to_csv(path_pais, index=False, decimal=",", sep=";")


def columnasCalculadas(path):
    dt = pd.read_csv(path, sep=";")
    dt['porc_iva'] = 0.21
    dt['iva'] = round(dt.porc_iva * dt.importe, 2)
    print(dt.head(3))
    dt['total'] = round(dt.iva + dt.importe, 2)
    dt2 = dt[['idpedido','idcliente','pais','importe','iva','total']]
    dt2.to_excel("../ficheros/pedidos.xslx")

if __name__ == "__main__":
    # exportarPaises('../ficheros_curso/merge/Pedidos.txt')
    columnasCalculadas("../ficheros_curso/merge/Pedidos.txt")
