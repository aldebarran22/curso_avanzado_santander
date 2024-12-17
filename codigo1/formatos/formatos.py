"""
Generar ficheros XML a partir de una colección de objetos de la BD
Serialización de objetos con: pickle, shelve
"""

from base_datos import Producto, Categoria, BaseDatos
from xml.etree.ElementTree import Element, SubElement, tostring, Comment

def generarXML(L, path):

    # Generar el nodo raiz:
    raiz = Element("productos")
    raiz.set("version", "1.0")
    comentario = Comment("Productos extraidos de la base de datos Empresa3.db")

    # Añadir el comentario al nodo raiz:
    raiz.append(comentario)

    # Generar un producto por cada objeto de la colección:
    for p in L:
        nodoProducto = SubElement(raiz, 'producto')
        nodoProducto.attrib['id'] = str(p.id)
        nodoNombre = SubElement(nodoProducto, 'nombre')
        nodoNombre.text = p.nombre
        nodoPrecio = SubElement(nodoProducto, 'precio')
        nodoPrecio.text = str(round(p.precio,2))
        nodoCat = SubElement(nodoProducto, 'categoria')
        nodoCat.attrib['idcat']=str(p.cat.id)
        nodoCat.text = p.cat.nombre
        nodoExistencias = SubElement(nodoProducto, 'existencias')
        nodoExistencias.text = str(p.exis)



    # Imprimir el árbol
    print(tostring(raiz, encoding='unicode'))

if __name__ == "__main__":
    try:
        bd = BaseDatos("empresa3.db")
        L = bd.select()
        generarXML(L, "../ficheros/productos.xml")

    except Exception as e:
        print(e)
