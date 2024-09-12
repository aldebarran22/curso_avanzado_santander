"""
Generar un fichero XML con contenido de la Base de datos.
Procesar el fichero mediante el parseador de SAX, y 
las consultas XPath.
"""

from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from base_datos import path, BaseDatos, Categoria, Producto

def exportarXML(pathFile):
    pass

if __name__ == '__main__':
    exportarXML("productos.xml")