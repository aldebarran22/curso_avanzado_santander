"""
Ejemplo de clase abstracta y funciones asociadas a las clases:
isinstance, issubclass, __subclasses__
"""

import abc
import math


class Figura(abc.ABC):

    def __init__(self, etiqueta="", color=0):
        self.etiqueta = etiqueta
        self.color = color

    @abc.abstractmethod
    def area(self):
        pass

    def __str__(self):
        return self.etiqueta + " " + str(self.color)
    
class Circulo(Figura):

    def __init__(self, etiqueta="", color=0, radio=5):
        super().__init__(etiqueta, color)
        self.radio = radio

    def __str__(self):
        return super().__str__() + " " + str(self.radio)

    def area(self):
        return math.pi * self.radio**2

if __name__ == "__main__":
    try:
        fig = Figura("circulo", 5)
    except Exception as e:
        print(e.__class__.__name__, e)
