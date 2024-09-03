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

Python es un lenguaje de POO dinámico, permite crear att. 
en t.de ejecución
"""


class Empleado:
    """Implementación clase empleado"""

    def __init__(self, id=0, nombre="", cargo=""):
        self.id = id
        self.nombre = nombre
        self.cargo = cargo

    def __str__(self):
        return str(self.id) + " " + self.nombre + " " + self.cargo
        # return " ".join([k+":"+str(v) for k,v in self.__dict__.items()])

    def __repr__(self):
        return str(self)

    def __lt__(self, otro):
        return self.nombre < otro.nombre

    def __del__(self):
        # print('borrando: ', self.nombre)
        pass


class EmpleadoEmpresa(Empleado):
    def __init__(self, id=0, nombre="", cargo="", sueldo=0.0, empresa=""):
        Empleado.__init__(self, id, nombre, cargo)
        # super().__init__(id, nombre, cargo)
        self.sueldo = sueldo
        self.empresa = empresa

    def __str__(self):
        return super().__str__() + " " + str(self.sueldo) + " " + self.empresa


def testEmpleado():
    emp = Empleado(1, "Ana", "Ventas")

    emp.telefono = 600363635
    emp.__dict__["fijo"] = 914586699
    print(emp, emp.__dict__)

    L = [emp, Empleado(2, "Gema", "Gerente"), Empleado(3, "Pablo", "Admin")]
    print(L)
    L.sort(key=lambda obj: obj.cargo)
    print(L)

    # Extraer los nombres de los empleados:
    nombres = [obj.nombre for obj in L]
    nombres.sort()
    print(nombres)

    # Ordenar con un criterio por defecto:
    L.sort()

    # Convertir a json
    Ljson = [obj.__dict__ for obj in L]
    print(Ljson)


def testEmpleadoEmpresa():
    emp2 = EmpleadoEmpresa(nombre="Ana", sueldo=2000.0, empresa="TRT")
    print(emp2)
    print(emp2.__class__.__name__)

    # Otra forma de crear un objeto en Python
    emp1 = emp2.__class__()
    print(emp1)

    s = "{}({},{},{})".format("Empleado", 0, "'Miguel'", "'Ventas'")
    print(s)
    obj = eval(s)
    print(obj, obj.__class__)


class Terrestre:
    def desplazar(self):
        print("El animal anda")


class Acuatico:
    def desplazar(self):
        print("El animal nada")


class Cocodrilo(Terrestre, Acuatico):
    def desplazar(self):
        Terrestre.desplazar(self)
        Acuatico.desplazar(self)


if __name__ == "__main__":
    testEmpleado()
