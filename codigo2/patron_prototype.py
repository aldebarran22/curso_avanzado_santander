"""
Patrón prototype. 
Implementar dos factorias de prototipos:
a) Inicializa todos los objetos al principio. Después en cada petición clona el prototipo
b) Inicializa los objetos bajo demanda. En la primera petición crea el objeto y luego
lo va clonando.
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
        return copy.deepcopy(self)


class Factoria1:
    """Crea todos los objetos al principio"""

    def __init__(self):
        self.prototipos = dict()
        for clase in Prototipo.__subclasses__():
            k = clase.__name__.lower()
            v = clase()
            self.prototipos[k] = v

    def get(self, etiqueta):
        k = etiqueta.lower()
        if k not in self.prototipos:
            raise KeyError(f"No existe el propotipo: {k}")
        else:
            return self.prototipos[k].clone()

    def print(self):
        print('\nPrototipos:')
        for k, v in self.prototipos.items():
            print(k, '==>', v)
        print()

class Factoria2:
    """Crea los objetos bajo demanda"""

    def __init__(self):
        self.prototipos = dict()
        for clase in Prototipo.__subclasses__():
            k = clase.__name__.lower()           
            self.prototipos[k] = None

    def get(self, etiqueta):
        k = etiqueta.lower()
        if k not in self.prototipos:
            raise KeyError(f"No existe el propotipo: {k}")
        else:
            if self.prototipos[k] is None:
                clase = etiqueta.capitalize()
                objeto = globals()[clase]()
                self.prototipos[k] = objeto

            return self.prototipos[k].clone()
        

    def print(self):
        print('\nPrototipos 2:')
        for k, v in self.prototipos.items():
            print(k, '==>', v)
        print()

def test(claseFactoria):

    factoria = claseFactoria()
    factoria.print()

    figura = factoria.get("circulo")
    figura.color = "green"
    figura.etiqueta = "hola"
    print('figura: ', figura)

    factoria.print()

if __name__=='__main__':
    # test(Factoria1)
    test(Factoria2)