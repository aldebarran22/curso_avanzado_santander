"""
Generar XML con el contenido de la BD
"""

from base_datos import Categoria, BaseDatos, path
from xml.etree.ElementTree import iterparse, Element, SubElement, Comment, tostring
from xml.etree import ElementTree


def generarXML():
    try:
        bd = BaseDatos(path)
        raiz = Element("categorias")
        raiz.set("version", "1.0")

        listaCategorias = bd.selectCategorias()
        for c in listaCategorias:
            categoria = SubElement(raiz, "categoria", {"idcat": str(c.id)})
            nombreCat = SubElement(categoria, "nombre")
            nombreCat.text = c.nombre

            productos = SubElement(categoria, "productos")
            listaProductos = bd.select(c.nombre)
            for p in listaProductos:
                producto = SubElement(productos, "producto", {"idprod": str(p.id)})
                nombreProd = SubElement(producto, "nombre")
                nombreProd.text = p.nombre

                precioProd = SubElement(producto, "precio")
                precioProd.text = str(p.precio)

                existenciasProd = SubElement(producto, "existencias")
                existenciasProd.text = str(p.exis)

        tree = ElementTree.ElementTree()
        tree._setroot(raiz)
        tree.write("productos.xml")
        print("Fichero generado: productos.xml")

    except Exception as e:
        print(e)


def procesarXML(path):
    with open(path, "r") as f:
        top = ElementTree.parse(f)
        raiz = top.getroot()
        # print(tostring(raiz))

        # Extraer los nombres de las categorias:
        for t in raiz.findall(".//categoria/nombre"):
            print(t.tag, t.text)

def procesarSAX(path):
    eventos = ["start","end"]
    for evento, nodo in iterparse(path, eventos):
        print(evento, nodo.tag)

if __name__ == "__main__":
    # generarXML()
    # procesarXML("productos.xml")
    procesarSAX("productos.xml")
