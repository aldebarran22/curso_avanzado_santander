"""
POO en Python

"""

class Producto:
    """Implementación de la clase producto"""

    def __init__(self, nombre="", precio=0):
        self.nombre = nombre
        self.precio = precio

    def __repr__(self):
        return str(self)
    
    """
    def __str__(self):
        return self.nombre+" "+str(self.precio)
    """

    def __str__(self):
        return ",".join([str(v) for v in self.__dict__.values()])


    def __lt__(self, other):
        """
        if p1 < p2:  -> if p1.__lt__(p2):
            pass
        """
        return self.precio < other.precio
    
    def __del__(self):
        print('Borrando ',self.nombre)
   
    
class Catalogo:
    
    def __init__(self, *args):
        self.lista = []
        self.lista.extend(args)

    def __len__(self):
        return len(self.lista)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        pass



def testProducto():
    p1 = Producto('CocaCola',2.5)    
    print(p1)

    L = [p1, Producto('Fanta Limón',1.7), Producto('cerveza',2.25)]
    print(L)

    L.sort(key=lambda p : p.nombre.lower())
    print(L)
    L.sort()
    print(L)

    if p1 < L[0]:
        print(p1,"menor que",L[0])
    else:
        print(L[0],"menor que",p1)

    # Atributos dinámicos:
    p1.iva = 0.21
    p1.__dict__['categoria'] = "Bebida"
    print(p1.__dict__)

    d = [p.__dict__ for p in L]
    print(d)
    print(p1)   

    # Crear otro objeto a partir de la clase de p1:
    p2 = p1.__class__()
    print("p2:",p2)

    p3 = p1.__class__('Carne',20.9)
    print("p3:",p3)

def testCatalogo():
    p1 = Producto('CocaCola',2.5)  
    p2 = Producto('Fanta Limón',1.7)
    p3 = Producto('cerveza',2.25)
    
    tienda = Catalogo(p1,p2,p3) # Catalogo(p1,p2)
    print('Tenemos: ', len(tienda), 'productos')
    for p in tienda:
        print(p)

if __name__ == "__main__":
    # testProducto()
    testCatalogo()

    
    

