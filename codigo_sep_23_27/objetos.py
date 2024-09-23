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
    
    def __repr__(self):
        return str(self)
    
    def __lt__(self,other):
        return self.precio < other.precio

class Tienda:

    def __init__(self, *listaProductos):
        self.productos = []
        self.productos.extend(listaProductos)
        self.__index = 0

    def __len__(self):
        return len(self.productos)

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__index == len(self.productos):
            raise StopIteration
        else:
            p = self.productos[self.__index]
            self.__index+=1
            return p

def testTienda():
    p1 = Producto(10, "CocaCola",1.5, 100)
    p2 = Producto(3, "Fanta", 2.3, 400)
    tienda = Tienda(p1, p2)
    print(len(tienda),'productos')
    for p in tienda:
        print(p)

def testProducto():
    p1 = Producto(10, "CocaCola",1.5, 100)
    p1.__dict__['iva']=round(p1.precio * 0.21,2)
    p1.descuento = 0.05
    print(p1) # p1.__str__()

    # Crear un objeto a partir de la clase de otro:
    p2 = p1.__class__(nombre="Vino",precio=12.5)
    print(p2)
    print(p2.__class__.__name__)

    L = [p1, p2, Producto(3, "Fanta", 2.3, 400)]
    print(L)
    L.sort(key=lambda obj : obj.nombre)
    print(L)
    L.sort(reverse=True)
    print(L)



if __name__ == '__main__':
    #testProducto()
    testTienda()
