"""
Generar formatos:
json
xml: DOM / SAX / XPath
Serialización:
- Pickle
- Shelve
"""

from base_datos import Categoria, Producto, BaseDatos
import json
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.etree import ElementTree

def exportarJson(L, path):
    """Exportar todos los productos con la categoría a un fichero json"""
    fich = None
    try:
        fich = open(path, 'w')
        R = [objeto.to_json() for objeto in L]
        json.dump(R, fich, indent=4)
        print(f'Se ha generado el fichero: {path}')

    except Exception as e:
        raise e
    
    finally:
        if fich:fich.close()


def importarJson(path):
    fich = None
    try:
        fich = open(path, 'r')
        R = json.load(fich)
        L = [Producto.create(d) for d in R]
        print(L[:3])
        return L

    except Exception as e:
        raise e
    
    finally:
        if fich:fich.close()

def exportarXML(L, path):
    nodoRaiz = Element("productos")
    nodoRaiz.set('version','1.0')
    comentario = Comment('Productos de la BD.')
    nodoRaiz.append(comentario)
    for producto in L:
        nodoProducto = SubElement(nodoRaiz, 'producto')
        nodoProducto.attrib['id']=str(producto.id)
        nodoNombre = SubElement(nodoProducto, 'nombre')
        nodoNombre.text = producto.nombre
        nodoPrecio = SubElement(nodoProducto, "precio")
        nodoPrecio.text = str(round(producto.precio, 2))
        nodoCat = SubElement(nodoProducto, 'categoria')
        nodoNombreCat = SubElement(nodoCat, 'nombre')
        nodoNombreCat.attrib['idcat'] = str(producto.cat.id)
        nodoNombreCat.text = producto.cat.nombre
        nodoExistencias = SubElement(nodoProducto, 'existencias')
        nodoExistencias.text = str(producto.exis)

    #print(tostring(nodoRaiz, encoding='unicode'))
    tree = ElementTree.ElementTree()
    tree._setroot(nodoRaiz)
    tree.write(path)
    print(f'Se ha generado el fichero: {path}')


def buscarXMLDom(path):
    with open(path,'rt') as f:
        tree = ElementTree.parse(f)
    raiz = tree.getroot()
    print('num nodo: ', len([n for n in raiz]))

    # Todos los valores de la etiqueta nombre a cualquier nivel del fichero:
    xpath = ".//nombre"
    L = [nodo.text for nodo in raiz.findall(xpath)]
    print(L)

    # Solo nombres de los productos:
    xpath = ".//producto/nombre"
    L = [nodo.text for nodo in raiz.findall(xpath)]
    print(L)

    # Solo nombres de las categorias
    xpath = ".//categoria/nombre"
    c = {nodo.text for nodo in raiz.findall(xpath)}
    print(sorted(c, key=lambda cad : cad.capitalize()))

       

if __name__ == '__main__':
    try:
        bd = BaseDatos("empresa3.db")
        L = bd.select()
        exportarJson(L, "productos.json")
        importarJson("productos.json")
        exportarXML(L, "productos.xml")
        buscarXMLDom("productos.xml")

    except Exception as e:
        print(e)
    
