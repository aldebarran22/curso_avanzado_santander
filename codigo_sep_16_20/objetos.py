"""
POO en python
"""

import copy
from collections import namedtuple

CuentaBancaria = namedtuple('CuentaBancaria',['entidad','sucursal','dc','cuenta'])


class Producto:
    """Implementación de la clase producto"""

    def __init__(self,id=0,nombre="",idcategoria=0,precio=0.0,exis=0):
        self.id = id
        self.nombre=nombre
        self.idcategoria=idcategoria
        self.precio=precio
        self.exis=exis

    def __str__(self):
        # str()
        return " ".join([str(i) for i in self.__dict__.values()])

    def __repr__(self):
        # repr()
        return str(self)

    def __lt__(self, other):
        return self.precio < other.precio

    def __del__(self):
        pass
        #print("Borrando ", self.nombre)

class Tienda:

    def __init__(self, *productos):
        self.catalogo = []
        self.catalogo.extend(productos)
        self.indice = -1

    def __len__(self):
        return len(self.catalogo)

    def __iter__(self):
        return self

    def __next__(self):
        if self.indice == len(self.catalogo):
            self.indice=-1
            raise StopIteration
        else:
            obj = self.catalogo[self.indice]
            self.indice+=1
            return obj


def testProducto():
    prod = Producto(1,"CocaCola",1, 2.5, 100)
    print(prod.__dict__)
    p2 = copy.deepcopy(prod)

    prod.descuento=0.25
    prod.__dict__["iva"]=0.21
    print(prod.__dict__)

    print(p2.__dict__)
    print(p2)
    print(prod)

def testListaProductos():
    prod = Producto(1,"CocaCola",1, 2.5, 100)
    prod2 = Producto(2,"Fanta ",1, 1.5, 130)
    prod3 = Producto(3,"Pepsi",1, 2.15, 100)
    L = [prod, prod3, prod2]
    print(L)
    L.sort(key=lambda obj : obj.nombre)
    print(L)
    L.sort()
    print(L)

    print(prod.__class__)
    print(prod.__class__.__name__)

    # Crear una instancia:
    p3 = prod.__class__(nombre="nuevo")
    print(p3)

    if prod < prod2: # if prod.__lt__(prod2)
        print("El menor es: ", prod)
    else:
        print("El menor es:", prod2)


def tuplaConNombre():
    cc1 = CuentaBancaria(1000,3434,99,12345678)
    #cc1.dc = 11 solo lectura
    print(cc1)
    print('entidad:',cc1.entidad)

def testIterable():
    prod = Producto(1,"CocaCola",1, 2.5, 100)
    prod2 = Producto(2,"Fanta ",1, 1.5, 130)
    prod3 = Producto(3,"Pepsi",1, 2.15, 100)
    L = [prod, prod3, prod2]

    for i in L:
        print(i)

def testTienda():
    prod = Producto(1,"CocaCola",1, 2.5, 100)
    prod2 = Producto(2,"Fanta ",1, 1.5, 130)
    prod3 = Producto(3,"Pepsi",1, 2.15, 100)
    t = Tienda(prod, prod2)
    print('Tenemos: ', len(t), 'productos')
    for p in t:
        print(p)

    print('Segunda vez')
    for p in t:
        print(p)


if __name__=='__main__':
    #testProducto()
    #testListaProductos()
    #tuplaConNombre()
    #testIterable()
    testTienda()




