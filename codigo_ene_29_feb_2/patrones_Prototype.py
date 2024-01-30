"""
Diseñar dos factorías (mantener un catálogo
de prototipos)
a) Se crean los prototipos al instanciar la factoria
b) Se crean bajo demanda.

Cada factoría tendrá un método para solicitar
un objeto y este será clonado.
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
        return copy.copy(self)


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
        return copy.copy(self)


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
        return copy.copy(self)


class Factoria1:
    """Mantiene los prototipos creados
    desde el principio"""

    def __init__(self, figura) -> None:
        # Mantenemos los prototipos en un dict
        # k: str -> v: instancia
        self.prototipos = dict()
        L = figura.__subclasses__()
        for c in L:
            self.prototipos[c.__name__] = c()

    def getPrototipo(self, nombre):
        # Localiza el prototipo y lo clona
        k = nombre.capitalize()
        if k not in self.prototipos:
            raise ValueError(f"No existe el prototipo:{nombre}")
        else:
            # Se clona:
            return self.prototipos[k].clone()

    def print(self):
        print("Prototipos:")
        for k, v in self.prototipos.items():
            print(k, v)


class Factoria2:
    """Crea los prototipos bajo demanda"""

    def __init__(self, figura) -> None:
        # Crear dict sin instanciar los prototipos
        self.prototipos = {c.__name__: None for c in figura.__subclasses__()}

    def getPrototipo(self, nombre):
        # Antes de clonar comprobar si ya está
        # creado el prototipo, si no, se crea
        # y al final se clona
        k = nombre.capitalize()
        if k not in self.prototipos:
            raise ValueError(f"No existe el prototipo:{nombre}")
        else:
            # Crear el prototipo:
            cad = f"{k}()"
            self.prototipos[k] = eval(cad)

            # Se clona:
            return self.prototipos[k].clone()

    def print(self):
        print("Prototipos:")
        for k, v in self.prototipos.items():
            print(k, v)


def testFactoria(claseFactoria):
    try:
        f = claseFactoria(Prototipo)
        f.print()
        print()
        p1 = f.getPrototipo("RECTANGULO")
        p1.color = "green"
        print(p1)
        print()
        f.print()

        p2 = f.getPrototipo("Rombo")
        print(p2)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    testFactoria(Factoria1)
