"""
Generar XML con el contenido de la BD
"""
from base_datos import Categoria, BaseDatos, path

def generarXML():
    try:
        bd = BaseDatos(path)
        listaCategorias = bd.selectCategorias()
        for c in listaCategorias:
            print(c.nombre)

            listaProductos = bd.select(c.nombre)
            for p in listaProductos:
                print("\t",p.nombre)
        

    except Exception as e:
        print(e)

if __name__ == '__main__':
    generarXML()