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
    """
    Al instanciar la factoria se crean TODOS los prototipos
    Y cada vez que se solicita un prototipo se clona
    """

    def __init__(self):
        """
        Definir la estructura de prototipos e inicializarlos
        """
        pass

    def getPrototipo(self, nombre):
        """
        Devuelve un clon del prototipo seleccionado
        """
        pass

    def print(self):
        """Imprimir el catalogo de prototipos"""
        pass


class Factoria2:
    """
    Al instanciar la factoria se NO crea los prototipos
    Y cada vez que se solicita un prototipo, se comprueba
    si ya existe, si no, se crea y luego siempre se clona.
    Crea los prototipos bajo demanda
    """

    def __init__(self):
        """
        Definir la estructura de prototipos y los inicializa a vacío
        """
        pass

    def getPrototipo(self, nombre):
        """
        Devuelve un clone del prototipo seleccionado, pero si no existe
        lo crea, y después lo clona
        """
        pass

    def print(self):
        """Imprimir el catalogo de prototipos"""
        pass


def testFactoria(factoria):
    try:
        f = factoria()
        f.print()
        obj1 = f.getPrototipo("CIRCULO")
        obj1.color = "red"
        obj1.radio = 7.5
        print(obj1)
        print("-" * 10)
        f.print()
    except Exception as e:
        print(e.__class__.__name__, e)


if __name__ == "__main__":
    # testFactoria(Factoria1)
    testFactoria(Factoria2)
