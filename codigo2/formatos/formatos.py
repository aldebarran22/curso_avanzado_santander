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

    print(tostring(nodoRaiz, encoding='unicode'))


if __name__ == '__main__':
    try:
        bd = BaseDatos("empresa3.db")
        L = bd.select()
        exportarJson(L, "productos.json")
        importarJson("productos.json")
        exportarXML(L, "productos.xml")

    except Exception as e:
        print(e)
    
