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
    
    def __str__(self):
        return self.nombre+" "+str(self.precio)
    
if __name__ == "__main__":
    p1 = Producto('CocaCola',2.5)    
    print(p1)

    L = [p1, Producto('Fanta Limón',1.7), Producto('Cerveza',2.25)]
    print(L)

