"""
Formas de crear objetos en Python
"""

class Punto:

    __slots__ = ("__x", "__y")

    
    def __init__(self, x, y):
            self.__x = x
            self.__y = y

    def setX(self, x):
            self.__x = x

    def setY(self, y):
            self.__y = y                

    def __str__(self):
            return str(self.__x) + ", " + str(self.__y)


def crearObjeto(clase, *args, **kwargs):
    return clase(*args, **kwargs)       

if __name__ == "__main__":
    # 1) Utilizar el constructor
    p1 = Punto(12,4)
    print(p1)
    #print(p1.__dict__) Falla no existe el dict

    # 2) A partir de una cadena de texto:
    cad = "{}({},{})".format("Punto",12,4)
    print(cad)
    p2 = eval(cad)
    print(p2)
    print(eval("1+4"))

    # 3) con la función crearObjeto
    p3 = crearObjeto(Punto, 12,4)
    print(p3)
    p4 = crearObjeto(Punto, x=12, y=4)
    print(p4)

    # 4) Con la funcion globals()
    print(globals())
    p5 = globals()["Punto"](12,4)
    print(p5)

    for k, v in globals().copy().items():
          print(k, type(v))

    # 5) Copiando el objeto: copia profunda
    import copy

    p6 = copy.deepcopy(p5)
    print(p6)