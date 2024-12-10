"""
Clases abstractas en Python
"""

import abc

class Figura(abc.ABC):

    def __init__(self, color="black", texto=""):
        self.color = color
        self.texto = texto

    def colorear(self, color):
        self.color = color

    @abc.abstractmethod
    def dibujar(self):
        pass

if __name__ == "__main__":
    fig = Figura("red", "etiqueta")