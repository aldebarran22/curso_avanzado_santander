"""
Generar ficheros en json y XML (dom)
Parsear documentos XML (SAX)
Búsquedas en documentos XML (Xpath)
"""
from base_datos import Empleado, Producto, Categoria
from base_datos import BaseDatos, path
import json

def exportarJSON(L, pathFich):
    pass

if __name__ == '__main__':
    bd = BaseDatos(path)
    L = bd.select()
    print(L)


