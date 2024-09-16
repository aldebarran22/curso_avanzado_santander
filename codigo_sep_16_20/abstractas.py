"""Clases abstractas en Python"""

import abc
import math

class Figura(abc.ABC):

    def __init__(self, etiqueta="", color=0):
        self.etiqueta=etiqueta
        self.color=color

    @abc.abstractmethod
    def area(self):
        pass

class Circulo(Figura):

    def __init__(self, etiqueta="", color=0, radio=0):
        Figura.__init__(self, etiqueta, color)
        self.radio=radio

    def area(self):
        return math.pi * self.radio**2

if __name__=='__main__':
    try:
        fig = Figura()
    except Exception as e:
        print(e)

    try:
        circulo = Circulo("C1", 5, 2.5)
        print(circulo.area())
    except Exception as e:
        print(e)