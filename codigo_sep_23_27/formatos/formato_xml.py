"""
Generar XML con el contenido de la BD
"""
from base_datos import Categoria, BaseDatos, path

def testBD():
    try:
        bd = BaseDatos(path)
        categorias = bd.selectCategorias()
        print(categorias)

    except Exception as e:
        print(e)

if __name__ == '__main__':
    testBD()