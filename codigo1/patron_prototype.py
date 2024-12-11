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
    """Inicializa todos los prototipos al principio"""

    def __init__(self):
        self.prototipos = dict()
        for c in Prototipo.__subclasses__():
            clave = c.__name__.lower()
            valor = c()
            self.prototipos[clave] = valor

    def get(self, clave):
        k = clave.lower()

        if k in self.prototipos:
            return self.prototipos[k].clone()
        else:
            raise KeyError("Prototipo no encontrado ...")

    def print(self):
        print("\nPrototipos:")
        for k, v in self.prototipos.items():
            print(k, " ", v)
        print()


class Factoria2:
    """Inicializa los prototipos bajo demanda, en la primera petición"""

    def __init__(self):
        self.prototipos = dict()

    def get(self, clave):
        nombreClase = clave.capitalize()
        nombreClave = clave.lower()

        if clave not in self.prototipos:
            # Buscar la clase:
            dicc = globals()
            if nombreClase in dicc:
                # Crear el objeto:
                obj = dicc[nombreClase]()
                self.prototipos[nombreClave] = obj

            else:
                raise ValueError("El prototipo no existe")
        
        return self.prototipos[nombreClave].clone()
               

    def print(self):
        print("\nPrototipos:")
        for k, v in self.prototipos.items():
            print(k, " ", v)
        print()


def test(claseFactoria):

    # Crear la factoria
    factoria = claseFactoria()

    # Imprimir el catálogo de prototipos:
    factoria.print()

    # Solicitar algún prototipo
    fig1 = factoria.get("circulo")
    fig1.radio *= 2
    fig1.color = "green"
    print(fig1)

    fig2 = factoria.get("circulo")
    fig2.radio *= 3
    fig2.color = "blue"
    print(fig2)

    fig3 = factoria.get("TRIANGULO")
    fig3.color = "white"
    print(fig3)

    factoria.print()


if __name__ == "__main__":
    # test(Factoria1)
    test(Factoria2)
