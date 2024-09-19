"""
Generar ficheros XML con Python. Lib xml
"""

from base_datos import Categoria, Producto, path, BaseDatos
from xml.etree.ElementTree import Element, SubElement, Comment, tostring

def exportarXML():
    try:
        raiz = Element("categorias", {"version":"1.0"})
        bd = BaseDatos(path)
        listaCat = bd.selectCategorias()

        for cat in listaCat:
            listaProd = bd.select(cat.nombre)

            for prod in listaProd:
                pass
        print(tostring(raiz))
            
    except Exception as e:
        print(e)


if __name__ == "__main__":
    exportarXML()
