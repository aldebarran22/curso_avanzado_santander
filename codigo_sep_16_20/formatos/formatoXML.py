"""
Generar ficheros XML con Python. Lib xml
"""

from base_datos import Categoria, Producto, path, BaseDatos
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.etree import ElementTree

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
        
                nombreProd = SubElement(producto, "nombre")
                nombreProd.text = prod.nombre

                precioProd = SubElement(producto, "precio")
                precioProd.text = str(prod.precio)

                exisProd = SubElement(producto, "existencias")
                exisProd.text = str(prod.exis)
        
        #print(tostring(raiz))
       
        tree = ElementTree.ElementTree()
        tree._setroot(raiz)
        tree.write('categorias.xml')
            
    except Exception as e:
        print(e)


def pruebaXPath():
    with open("categorias.xml",'rt') as f:
        tree = ElementTree.parse(f)
    raiz = tree.getroot()
    print(tostring(raiz))

if __name__ == "__main__":
    #exportarXML()
    pruebaXPath()
