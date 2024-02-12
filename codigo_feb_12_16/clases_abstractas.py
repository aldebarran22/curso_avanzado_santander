"""
Clases abstractas en Python
"""

import abc


class Figura(abc.ABC):

    def __init__(self, etiqueta="", color="black"):
        self.etiqueta = etiqueta
        self.color = color

    def __str__(self):
        return self.etiqueta + " " + self.color

    @abc.abstractmethod
    def calcularArea(self):
        pass


class Triangulo(Figura):

    def __init__(self, etiqueta="", color="black", b=0, h=0):
        Figura.__init__(self, etiqueta, color)
        self.b = b
        self.h = h

    def __str__(self):
        return Figura.__str__(self) + " " + str(self.b) + " " + str(self.h)

    def calcularArea(self):
        return (self.b * self.h) / 2.0


if __name__ == "__main__":
    f = Triangulo("T1", "red", 10, 20)
    print(f)
    print(f.calcularArea())
