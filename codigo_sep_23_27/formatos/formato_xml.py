"""
Generar XML con el contenido de la BD
"""
from base_datos import Categoria, BaseDatos, path
from xml.etree.ElementTree import Element, SubElement, Comment, tostring

def generarXML():
    try:
        bd = BaseDatos(path)
        raiz = Element('categorias')
        raiz.set('version','1.0')

        listaCategorias = bd.selectCategorias()
        for c in listaCategorias:
            categoria = SubElement(raiz, "categoria",\
                                   {"idcat":str(c.id)})
            nombreCat = SubElement(categoria, "nombre")
            nombreCat.text = c.nombre

            productos = SubElement(categoria, "productos")            
            listaProductos = bd.select(c.nombre)
            for p in listaProductos:
                producto = SubElement(productos, "producto", \
                                      {"idprod":str(p.id)})
                nombreProd = SubElement(producto, "nombre")
                nombreProd.text = p.nombre

                precioProd = SubElement(producto, "precio")
                precioProd.text = str(p.precio)

                existenciasProd = SubElement(producto, "existencias")
                existenciasProd.text = str(p.exis)
        
        print(tostring(raiz))

    except Exception as e:
        print(e)

if __name__ == '__main__':
    generarXML()