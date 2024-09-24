"""
Patrón prototype implementando dos factorías con estrategias distintas:
Factoria1 -> al crear la factoría se crean los prototipos. 
Factoria2 -> Los prototipos se crean bajo demanda.
"""

import abc
import math
import copy


class Figura(abc.ABC):

    def __init__(self, etiqueta="", color=0):
        self.etiqueta = etiqueta
        self.color = color

    @abc.abstractmethod
    def area(self):
        pass

    def __str__(self):
        return self.etiqueta + " " + str(self.color)

    @abc.abstractmethod
    def clonar(self):
        pass


class Circulo(Figura):

    def __init__(self, etiqueta="circulo", color=0, radio=5):
        super().__init__(etiqueta, color)
        self.radio = radio

    def __str__(self):
        return super().__str__() + " " + str(self.radio)

    def area(self):
        return math.pi * self.radio**2

    def clonar(self):
        return copy.deepcopy(self)


class Rectangulo(Figura):
    def __init__(self, etiqueta="rectangulo", color=0, ancho=5.0, alto=10.0):
        Figura.__init__(self, etiqueta, color)
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

    def area(self):
        return self.ancho * self.alto

    def clonar(self):
        return copy.deepcopy(self)


class Triangulo(Figura):
    def __init__(self, etiqueta="triangulo", color=0, base=2.5, altura=8.0):
        Figura.__init__(self, etiqueta, color)
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

    def area(self):
        return (self.base * self.altura) / 2

    def clonar(self):
        return copy.deepcopy(self)


class FactoriaPrototipos(abc.ABC):

    @abc.abstractmethod
    def inicializarPrototipos(self):
        pass

    @abc.abstractmethod
    def getPrototipo(self, key):
        pass

    @abc.abstractmethod
    def print(self):
        pass


class Factoria1(FactoriaPrototipos):
    """Extrategia: crear todos los objetos al principio"""

    def __init__(self):
        self.prototipos = None

    def inicializarPrototipos(self):
        self.prototipos = {c.__name__.lower():c() for c in Figura.__subclasses__()}

    def getPrototipo(self, key):
        k = key.lower()
        if k not in self.prototipos:
            raise KeyError(f"La clave {key} no se encuentra en los prototipos")
        else:
            # Clonar el prototipo:
            return self.prototipos[k].clonar()

    def print(self):
        print("Factoria1:")
        for k, v in self.prototipos.items():
            print(k,v)
        print()


class Factoria2(FactoriaPrototipos):
    """Extrategia: crear el objeto bajo demanda"""

    def __init__(self):
        self.prototipos = None

    def inicializarPrototipos(self):
        self.prototipos = {c.__name__.lower():None for c in Figura.__subclasses__()}

    def getPrototipo(self, key):
        k = key.lower()
        if k not in self.prototipos:
            raise KeyError(f"La clave {key} no se encuentra en los prototipos")
        
        elif self.prototipos[k] is None:
            # Crear el prototipo:
            nombreClase = k.capitalize()
            obj = eval(nombreClase+"()")
            self.prototipos[k] = obj

        return self.prototipos[k].clonar()

    def print(self):
        pass

def testFactoria(clase):
    fact = clase()
    fact.inicializarPrototipos()
    fact.print()
    obj = fact.getPrototipo("circulo")
    obj.radio *= 2
    print(obj)
    fact.print()



if __name__ == "__main__":
    testFactoria(Factoria1)
    #testFactoria(Factoria2)

