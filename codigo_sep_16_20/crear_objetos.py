"""
Distintas formas de crear objetos en Python
"""

class Punto:

    # Atributos de la clase
    __slots__ = ("x", "y")

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"[{self.x},{self.y}]"


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

    # 


