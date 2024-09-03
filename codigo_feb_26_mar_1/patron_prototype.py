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
        self.prototipos = {c.__name__.lower(): c() for c in Prototipo.__subclasses__()}

    def getPrototipo(self, nombre):
        """
        Devuelve un clon del prototipo seleccionado
        """
        clave = nombre.lower()
        if clave not in self.prototipos:
            raise ValueError(f"{nombre} no existe en la factoria")
        else:
            return self.prototipos[clave].clone()

    def print(self):
        """Imprimir el catalogo de prototipos"""
        print("Prototipos:")
        for nombre, objeto in self.prototipos.items():
            print(nombre, objeto)


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
        self.prototipos = {c.__name__.lower(): None for c in Prototipo.__subclasses__()}

    def getPrototipo(self, nombre):
        """
        Devuelve un clone del prototipo seleccionado, pero si no existe
        lo crea, y después lo clona
        """
        clave = nombre.lower()
        # Si la clave no esta es un error
        if clave not in self.prototipos:
            raise ValueError(f"{nombre} no existe en la factoria")

        else:
            # La clave existe, ¿está creado el objeto?
            if not self.prototipos[clave]:

                # hay que crear el objeto. Localizar la clase
                clase = nombre.capitalize()

                # Comprobar si la clase existe en globals()
                # if clase in globals().copy():
                clasePrototipo = globals()[clase]
                objeto = clasePrototipo()
                self.prototipos[clave] = objeto

        return self.prototipos[clave].clone()

    def print(self):
        """Imprimir el catalogo de prototipos"""
        print("Prototipos:")
        for nombre, objeto in self.prototipos.items():
            print(nombre, objeto)


def testFactoria(factoria):
    try:
        f = factoria()
        f.print()
        obj1 = f.getPrototipo("CIRCULO")
        obj1.color = "red"
        obj1.radio = 7.5
        print("NUEVO:", obj1)
        obj2 = f.getPrototipo("circulo")
        obj3 = f.getPrototipo("esfera")
        print("-" * 10)
        f.print()
    except Exception as e:
        print(e.__class__.__name__, e)


if __name__ == "__main__":
    # testFactoria(Factoria1)
    testFactoria(Factoria2)
