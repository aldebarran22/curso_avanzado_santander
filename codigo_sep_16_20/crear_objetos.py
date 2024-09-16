"""
Distintas formas de crear objetos en Python
"""

from copy import deepcopy
import sys

class Punto:

    # Atributos de la clase
    __slots__ = ("x", "y")

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"[{self.x},{self.y}]"


def create(clase, *args, **kwargs):
    return clase(*args, **kwargs)


if __name__=='__main__':

    # Llamando al constructor:
    p1 = Punto(1,2)
    print(p1)

    # Utilizando el class del objeto:
    p2 = p1.__class__(1,2)
    print(p2)

    # Crear un objeto a partir de una cadena: Punto(1,2)
    cad = "{}({},{})".format("Punto",1,2)
    print(cad)
    p3 = eval(cad)
    print(p3)

    # A partir de la función create
    p4 = create(Punto, 1,2)
    p5 = create(Punto, x=1,y=2)
    print(p4)
    print(p5)

    # Clonar un objeto:
    p6 = deepcopy(p1)
    print(p6)

    # Con la función globals:
    #print(globals())
    p7 = globals()['Punto'](1,2)
    print(p7)

    # A partir de la sys.modules
    p8 = getattr(sys.modules[__name__],"Punto")(1,2)
    print(p8)


