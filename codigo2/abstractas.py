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

class Circulo(Figura):

    def __init__(self, color="black", texto="", radio=5):
        Figura.__init__(self, color, texto)
        self.radio = radio

    def dibujar(self):
        print(self.color, self.texto, self.radio)

if __name__ == "__main__":
    fig = Circulo("red", "etiqueta", 10)
    fig.dibujar()