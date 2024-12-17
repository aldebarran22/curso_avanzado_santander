"""
Generar ficheros XML a partir de una colección de objetos de la BD
Serialización de objetos con: pickle, shelve
"""

from base_datos import Producto, Categoria, BaseDatos


def generarXML(L, path):
    pass


if __name__ == "__main__":
    try:
        bd = BaseDatos("empresa3.db")
        L = bd.select()
        generarXML(L, "../ficheros/productos.xml")

    except Exception as e:
        print(e)
