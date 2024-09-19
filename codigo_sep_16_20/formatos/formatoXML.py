"""
Generar ficheros XML con Python. Lib xml
"""

from base_datos import Categoria, Producto, path, BaseDatos
from xml.etree.ElementTree import iterparse, Element, SubElement, Comment, tostring
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

    # Consulta xpath:
    """
    for nodo in raiz.findall(".//producto/nombre"):
        print(nodo.text)
    """
    # Consulta xpath:
    for nodo in raiz.findall(".//nombre"):
        print(nodo.text)

def parsearSAX():
    # Extraer los nombres de las categorias
    eventos = ['start', 'end']
    categorias = []
    for (evento, nodo) in iterparse("categorias.xml", eventos):

        if evento == 'start':
            if nodo.tag == 'categoria':
                flag = True

            if nodo.tag == 'nombre' and flag:
                categorias.append(nodo.text)

            if nodo.tag == 'producto':
                flag = False

    print(categorias)


if __name__ == "__main__":
    #exportarXML()
    #pruebaXPath()
    parsearSAX()
