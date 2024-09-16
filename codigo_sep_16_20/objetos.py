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
        return " ".join([str(i) for i in self.__dict__.values()])

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


if __name__=='__main__':
    testProducto()


