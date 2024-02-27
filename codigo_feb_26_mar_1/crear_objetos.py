# -*- coding: cp1252 -*-
import sys, copy

# Python soporta NUMEROSAS FORMAS DE CREAR OBJETOS

# Partimos de la clase Punto:


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


def make_object(Class, *args, **kwargs):
    # print args
    # print kwargs
    print("*args", *args)
    return Class(*args, **kwargs)


# DISTINTAS FORMAS DE CREAR OBJETOS EN PYTHON

# Forma convencional llamando al constructor
p1 = Punto(8, 6)
print("p1:", p1)


# Se inyecta el cada {} un parámetro
p2 = eval("{}({},{})".format("Punto", 2, 4))  # "Punto(2,4)"
print("p2:", p2)


print(sys.modules[__name__], type(sys.modules[__name__]))
clase = getattr(sys.modules[__name__], "Punto")
print("clase: ", clase)
p3 = clase(7, 6) # La variable clase: almacena la clase Punto
print("p3:", p3)



# De todas las variables globales, seleccionar Punto
print(type(globals()))
d = globals().copy()
for k,v in d.items():
    print(k,"==>",v)


p4 = globals()["Punto"](3, 2)
print("p4:", p4)


# Con la funcion make_object, instancia la clase pasada por argumento
p5 = make_object(Punto, 4, 44)
print("p5:", p5)

# Copiando el objeto y modificando sus atts.
p6 = copy.deepcopy(p5)

# Revisar NO modifica:
p6.setX(98)
p6.setY(44)
print("p6:", p6)


# A partir del class de un objeto
print(p1.__class__)
p7 = p1.__class__(8, 99)
print("p7:", p7)

#print(globals())


def suma(a, b):
    return a + b


t = (1, 2)
print(suma(*t))
d = {"a": 1, "b": 2}
print(suma(**d))
