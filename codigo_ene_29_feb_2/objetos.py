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

Acceso a los atributos (encapsulación)
__privado
publico

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

Propiedades de los objetos:
__class__.__name__
__doc__
__dict__ --> los atributos: keys, y los valores: values
"""

class Empleado:
    """Implementación clase empleado"""

    def __init__(self, id=0, nombre="", cargo=""):
        self.id = id
        self.nombre = nombre
        self.cargo = cargo

    def __str__(self):
        return str(self.id) + " " + self.nombre + " " + self.cargo

    def __repr__(self):
        return str(self)

if __name__=='__main__':
    emp = Empleado(1, "Ana","Ventas")
    print(emp)
    L = [emp, Empleado(2,"Gema","Gerente"), Empleado(3,"Pablo","Admin")]
    print(L)
