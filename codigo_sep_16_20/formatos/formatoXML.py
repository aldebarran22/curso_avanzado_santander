"""
Generar ficheros XML con Python. Lib xml
"""

from base_datos import Categoria, Producto, path, BaseDatos


def exportarXML():
    try:
        bd = BaseDatos(path)
        listaCat = bd.selectCategorias()

        for cat in listaCat:
            listaProd = bd.select(cat.nombre)

            for prod in listaProd:
                pass
            
    except Exception as e:
        print(e)


if __name__ == "__main__":
    exportarXML()
