"""
POO en python
"""

class Producto:
    """Implementación de la clase producto"""

    def __init__(self,id=0,nombre="",idcategoria=0,precio=0.0,exis=0):
        self.id = id
        self.nombre=nombre
        self.idcategoria=idcategoria
        self.precio=precio
        self.exis=exis

def testProducto():
    prod = Producto(1,"CocaCola",1, 2.5, 100)
    print(prod.__dict__)
    prod.descuento=0.25
    prod.__dict__["iva"]=0.21
    print(prod.__dict__)

if __name__=='__main__':
    testProducto()

    
