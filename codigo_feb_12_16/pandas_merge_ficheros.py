"""
Pandas: merge
Fusionar por filas los ficheros: Pedidos, Empleados
y Empresas
"""

import pandas as pd
import sys


def mezcla():
    # Cargar los 3 ficheros:
    dfPedidos = pd.read_csv("pandas_ficheros/Pedidos.txt", sep=";")
    dfEmpleados = pd.read_csv("pandas_ficheros/Empleados.txt", sep=";")
    dfEmpresas = pd.read_csv("pandas_ficheros/Empresas.txt", sep=";")

    print("Pedidos:", dfPedidos.shape)
    print("Empleados:", dfEmpleados.shape)
    print("Empresas:", dfEmpresas.shape)

    dfTotal = pd.merge(dfPedidos, dfEmpleados, left_on="idempleado", right_on="id")

    dfTotal = dfTotal.merge(dfEmpresas, left_on="idempresa", right_on="id")

    dfTotal.drop(columns=["idempleado", "idempresa", "id_x", "id_y"], inplace=True)
    dfTotal.rename(columns={"nombre": "empleado"}, inplace=True)
    print(dfTotal.columns)
    dfTotal.to_html("ficheros/pedidos.html", index=False)


if __name__ == "__main__":
    mezcla()
