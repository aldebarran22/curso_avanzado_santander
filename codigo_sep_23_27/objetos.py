"""
POO en python
"""

class Producto:
    """Implementación de la clase producto"""

    def __init__(self, id=0, nombre="", precio=0.0, exis=0):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.exis = exis

    def __str__(self):
        return " ".join(k + "=" + str(v) for k, v in self.__dict__.items())


def testProducto():
    p1 = Producto(10, "CocaCola",1.5, 100)
    p1.__dict__['iva']=round(p1.precio * 0.21,2)
    p1.descuento = 0.05
    print(p1) # p1.__str__()

if __name__ == '__main__':
    testProducto()
