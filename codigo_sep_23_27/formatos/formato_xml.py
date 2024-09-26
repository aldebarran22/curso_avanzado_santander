"""
Generar XML con el contenido de la BD
"""
from base_datos import Categoria, BaseDatos, path

def testBD():
    try:
        bd = BaseDatos(path)
        categorias = bd.selectCategorias()
        print(categorias)

        productos = bd.select("Bebidas")
        print(productos[:3])

    except Exception as e:
        print(e)

if __name__ == '__main__':
    testBD()