"""
Generar un fichero XML con contenido de la Base de datos.
Procesar el fichero mediante el parseador de SAX, y 
las consultas XPath.
"""

from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from base_datos import path, BaseDatos, Categoria, Producto

def exportarXML(pathFile):
    try:
        bd = BaseDatos(path)
        categorias = bd.selectCategorias()
        raiz = Element("categorias")
        raiz.set("version","1.0")
        comentario = Comment("Categorias y productos de la BD")
        raiz.append(comentario)
        for cat in categorias:
            categoria = SubElement(raiz, "categoria")
            nombreCategoria = SubElement(categoria, "nombre")
            nombreCategoria.text = cat.nombre

        print(tostring(raiz))

    except Exception as e:
        print(e)

if __name__ == '__main__':
    exportarXML("productos.xml")