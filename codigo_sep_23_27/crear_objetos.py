"""Distintas formas de crear objetos en Python"""

class Punto:

    # Atributos de la clase
    __slots__ = ("x", "y")

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"[{self.x},{self.y}]"
    
def crearObjeto(clase, *args, **kwargs):
    return clase(*args, **kwargs)
    
if __name__ == '__main__':
    # Llamando al constructor
    p1 = Punto(1,2)
    print(p1)

    # A partir de la clase de otro objeto
    p2 = p1.__class__(1,2)
    print(p2)

    # A partir de una cadena:
    cad = "{}({},{})".format("Punto",1,2)
    print(cad)
    p3 = eval(cad)
    print(p3)

    p4 = crearObjeto(Punto, 1,2)
    p5 = crearObjeto(Punto, x=1,y=2)
    print(p4)
    print(p5)


