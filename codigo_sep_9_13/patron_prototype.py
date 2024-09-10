"""
Implementación el patrón prototype 
Disponemos de una serie de Figuras que se van a clonar mediante
una factoría.

Dos estrategias posible:
a) La factoría crea todos los prototipos al principio.
b) La factoría crea los prototipos bajo demanda.
"""

import abc
import copy


class Prototipo(abc.ABC):
    def __init__(self, etiqueta="", color="black"):
        self.etiqueta = etiqueta
        self.color = color

    def __str__(self):
        return "etiqueta: " + self.etiqueta + " color: " + self.color

    @abc.abstractmethod
    def clone(self):
        pass


class Circulo(Prototipo):
    def __init__(self, etiqueta="circulo", color="black", radio=5.0):
        Prototipo.__init__(self, etiqueta, color)
        self.radio = radio

    def __str__(self):
        return super().__str__() + " radio: " + str(self.radio)

    def clone(self):
        # El objeto se clona
        return copy.deepcopy(self)


class Rectangulo(Prototipo):
    def __init__(self, etiqueta="rectangulo", color="black", ancho=5.0, alto=10.0):
        Prototipo.__init__(self, etiqueta, color)
        self.ancho = ancho
        self.alto = alto

    def __str__(self):
        return (
            super().__str__()
            + " ancho: "
            + str(self.ancho)
            + " alto: "
            + str(self.alto)
        )

    def clone(self):
        # El objeto se clona
        return copy.deepcopy(self)


class Triangulo(Prototipo):
    def __init__(self, etiqueta="triangulo", color="black", base=2.5, altura=8.0):
        Prototipo.__init__(self, etiqueta, color)
        self.base = base
        self.altura = altura

    def __str__(self):
        return (
            super().__str__()
            + " base: "
            + str(self.base)
            + " altura: "
            + str(self.altura)
        )

    def clone(self):
        # El objeto se clona
        return copy.deepcopy(self)


class Factoria1:
    """Mantiene el catálogo de prototipos.
    La factoría crea todos los prototipos al principio"""

    def __init__(self):
        """Definir la estructura de prototipos e inicializarlos"""
        
        # Utilizamos las subclases de prototipo y cargamos el dict
        # con clave: nombre de la clase y el valor una instancia.
        self.prototipos = {c.__name__.lower() : c() for c in Prototipo.__subclasses__()}

    def getPrototipo(self, nombre):
        """Devuelve un clon del prototipo seleccionado.
        Ya estaba creado previamente"""
        if nombre.lower() in self.prototipos:
            return self.prototipos[nombre.lower()].clone()
        else:
            raise ValueError(f"Prototipo {nombre} no existe ...")

    def print(self):
        """Imprime los objetos de la factoria"""
        print("Factoria1:")
        for k,v in self.prototipos.items():
            print(k, v)



class Factoria2:
    """Mantiene el catálogo de prototipos.
    La factoría crea los prototipos bajo demanda"""

    def __init__(self) -> None:
        """Definir la estructura de prototipos e inicializarlos"""
        pass

    def getPrototipo(self, nombre):
        """Devuelve un clon del prototipo seleccionado, pero si no existe
        lo crea, y después lo clona"""
        pass

    def print(self):
        """Imprime los objetos de la factoria"""
        pass


if __name__ == '__main__':
    fact1 = Factoria1()
    fact1.print()
    obj = fact1.getPrototipo("circulo")
    obj.radio = 10
    obj.color = "orange"
    print("obj clonado: ",obj)
    fact1.print()