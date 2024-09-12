"""
Generar un fichero XML con contenido de la Base de datos.
Procesar el fichero mediante el parseador de SAX, y 
las consultas XPath.
"""

from xml.etree import ElementTree
from xml.etree.ElementTree import iterparse, Element, SubElement, Comment, tostring
from base_datos import path, BaseDatos, Categoria, Producto

def importarXML_SAX(pathFile):
    """Recuperar los nombres de las categorias"""
    categorias = []
    eventos = ['start','end']
    for (evento, nodo) in iterparse(pathFile, eventos):
        print(evento, nodo)

    print(categorias)

def importarXML_XPath(pathFile):
    """Importar el fichero con el DOM e imprimir los nombres
    de las categorias con Xpath"""
    with open(pathFile, "rt") as f:
        tree = ElementTree.parse(f)
        raiz = tree.getroot()
        for t in raiz.findall(".//categoria/nombre"):
            print(t.text)

def importarXML_Dom(pathFile):
    """Importar el fichero con el DOM e imprimir los nombres
    de las categorias"""
    with open(pathFile, "rt") as f:
        tree = ElementTree.parse(f)
        raiz = tree.getroot()
        categorias = raiz.getchildren()
        for c in categorias:
            print(c.getchildren()[0].text)

def exportarXML(pathFile):
    try:
        bd = BaseDatos(path)
        categorias = bd.selectCategorias()
        raiz = Element("categorias")
        raiz.set("version","1.0")
        comentario = Comment("Categorias y productos de la BD")
        raiz.append(comentario)
        for cat in categorias:
            nodoCategoria = SubElement(raiz, "categoria",  {"id":str(cat.id)})
            nombreCategoria = SubElement(nodoCategoria, "nombre")
            nombreCategoria.text = cat.nombre

            # Recuperar los productos de cada categoría:
            productos = bd.select(cat.nombre)
            nodoProductos = SubElement(nodoCategoria, "productos")

            for prod in productos:
                nodoProducto = SubElement(nodoProductos,"producto", {"id":str(prod.id)})

                nombreProducto = SubElement(nodoProducto, "nombre")
                nombreProducto.text = prod.nombre

                precioProducto = SubElement(nodoProducto, "precio")
                precioProducto.text = str(prod.precio)

                exisProducto = SubElement(nodoProducto, "existencias")
                exisProducto.text = str(prod.exis)

        #print(tostring(raiz))

        # Grabar al fichero:
        tree = ElementTree.ElementTree()
        tree._setroot(raiz)
        tree.write(pathFile)

    except Exception as e:
        print(e)

if __name__ == '__main__':
    #exportarXML("productos.xml")
    #importarXML_Dom("productos.xml")
    #importarXML_XPath("productos.xml")
    importarXML_SAX("productos.xml")
