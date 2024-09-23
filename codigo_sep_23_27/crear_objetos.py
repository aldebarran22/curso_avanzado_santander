"""Distintas formas de crear objetos en Python"""

class Punto:

    # Atributos de la clase
    __slots__ = ("x", "y")

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"[{self.x},{self.y}]"
    
if __name__ == '__main__':
    p1 = Punto(1,2)
    print(p1)

    p2 = p1.__class__(1,2)
    print(p2)