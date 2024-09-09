"""
Clases abstractas en Python.
"""

import abc


class Figura(abc.ABC):

    def __init__(self, etiqueta="", color=0):
        self.color = color
        self.etiqueta = etiqueta

    def __str__(self):
        return self.etiqueta + " " + str(self.color)

    @abc.abstractmethod
    def area(self):
        pass


class Triangulo(Figura):

    def __init__(self, etiqueta="", color=0, base=0, altura=0):
        Figura.__init__(self, etiqueta, color)
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

    def __str__(self):
        return Figura.__str__(self) + " B:" + str(self.base) + " H:" + str(self.altura)+ " A: "+str(self.area())


if __name__ == "__main__":
    try:
        fig = Figura("F1")
    except Exception as e:
        print(e)

    t1 = Triangulo("t1", 5, 3.5,6.0)
    print(t1)
