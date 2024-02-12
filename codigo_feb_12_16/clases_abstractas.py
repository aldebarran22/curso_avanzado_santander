"""
Clases abstractas en Python
"""

import abc

class Figura(abc.ABC):

    def __init__(self, etiqueta="", color="black"):
        self.etiqueta = etiqueta
        self.color = color

    @abc.abstractmethod
    def calcularArea(self):
        pass

if __name__ == '__main__':
    f = Figura("Triangulo", "red")
    