"""
Formas de crear y copiar objetos en Python
"""


class Punto:

    __slots__ = ("__x", "__y")

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"[{self.__x},{self.__y}]"

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

if __name__=='__main__':

    # Llamar al constructor de la clase:
    p1 = Punto(1,5)
    print("p1",p1, p1.__class__.__name__)

    # Crear el obj. a partir de str:
    nombreClase = "Punto"
    sentencia = "{}({},{})".format(nombreClase, 1,5)
    print(sentencia)
    p2 = eval(sentencia)
    print("p2",p2, p2.__class__.__name__)
