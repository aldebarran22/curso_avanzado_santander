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
            categoria = SubElement(raiz, "categoria",{"idcat":str(cat.id)})
            nombreCat = SubElement(categoria, "nombre")
            nombreCat.text = cat.nombre

            listaProd = bd.select(cat.nombre)
            productos = SubElement(categoria, "productos")

            for prod in listaProd:
                producto = SubElement(productos, "producto", {"idprod":str(prod.id)})
        
        
        print(tostring(raiz))
            
    except Exception as e:
        print(e)


if __name__ == "__main__":
    exportarXML()