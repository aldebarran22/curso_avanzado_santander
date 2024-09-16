"""
POO en python
"""

import copy

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
    L.sort(key=lambda obj : obj.precio)
    print(L)


if __name__=='__main__':
    #testProducto()
    testListaProductos()


