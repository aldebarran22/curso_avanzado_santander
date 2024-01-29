"""
POO en python
Soporta: herencia simple y múltiple
sobrecarga de operadores:
< <= == >= > !=
__lt__, __le__, ... __eq__ ...
Necesarios si queremos ordenar una lista de objetos de la clase. <
TypeError

+ -
__add__, __sub__ ...
r = obj1 + obj2 # r = obj1.__add__(obj2)

Clases abstractas (si). abc
@abc.abstractmethod

En python: no existen interfaces

El objeto en curso: self (equivale a this)
Una ref a la clase se obtiene con cls

tipos de métodos:
- de instancia (primer parámetro self)
- de clase  (primer parámetros cls) @classmethod
- estáticos (ni self ni cls)        @staticmethod

Comunicación con la clase Padre:
super().__str__()
ClasePadre.__str__(self)

atributos:
- de instancia (se definen con self)
    dentro del constructor
- de clase

constructor:
- __init__, si no se indica se especifica uno por defecto
destructor
- __del__

superclase es: object

funciones especiales - funciones del lenguaje
__str__()               str()
__repr__()              repr()
__del__()               del()
instancia = Clase()
del(instancia) --> instancia.__del__()
"""