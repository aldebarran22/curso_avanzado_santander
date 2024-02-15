"""
Pandas: merge
Fusionar por filas los ficheros: Pedidos, Empleados
y Empresas
"""

import pandas as pd


def mezcla():
    # Cargar los 3 ficheros:
    dfPedidos = pd.read_csv("pandas_ficheros/Pedidos.txt", sep=";")
    dfEmpleados = pd.read_csv("pandas_ficheros/Empleados.txt", sep=";")
    dfEmpresas = pd.read_csv("pandas_ficheros/Empresas.txt", sep=";")

    print("Pedidos:", dfPedidos.shape)
    print("Empleados:", dfEmpleados.shape)
    print("Empresas:", dfEmpresas.shape)


if __name__ == "__main__":
    mezcla()
