"""
Testear el módulo de BD con las operaciones CRUD
C - Create -> insert (HTTP POST)
R - Read -> select (HTTP GET)
U - Update -> update (HTTP PUT)
D - Delete -> delete (HTTP DELETE)
"""

from base_datos import BaseDatos, Producto, Categoria, path

def testCreate():
    try:
        bd = BaseDatos(path)
        cat = bd.readCategoria("Bebidas")
        if cat:
            prod = Producto(0, "RedBull 2", cat, 2.3, 100)
            n = bd.create(prod)
            if n == 1:
                print('Producto creado ...')
            else:
                print('No se ha podido crear')
        else:
            print('No se ha cargado la categoría')

    except Exception as e:
        print(e)

if __name__ == '__main__':
    testCreate()