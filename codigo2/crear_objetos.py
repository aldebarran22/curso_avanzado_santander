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
    
if __name__=="__main__":
       
    #1)Con el constructor
    p1 = Punto(12, 5)
    print(p1)

    #2) Con el class de un objeto:
    p2 = p1.__class__(12,5)
    print(p2)

    #3) A partir de una cadena de texto:
    cad = "{}({},{})".format('Punto', 12, 5)
    print(cad, type(cad))
    p3 = eval(cad)
    print(p3)

    #4) A partir de una función que recibe la clase y los parámetros:
    p4 = crearObjeto(Punto, 12, 5)
    print(p4)
    p5 = crearObjeto(Punto, x = 12, y = 4)
    print(p5)

    #5) Con la función globals()
    for k, v in globals().copy().items():
          print(k,v)
    p6 = globals()['Punto'](12, 4)
    print(p6)

    #6) A partir de sys.modules
    import sys

    p7 = getattr(sys.modules[__name__], 'Punto')(12, 4)    
    print(p7)

    print(sys.modules.keys())