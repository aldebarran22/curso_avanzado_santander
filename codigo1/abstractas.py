"""
Crear clases abstractas en Python
"""

import abc

class Figura(abc.ABC):

    def __init__(self, texto="", color="black"):
        self.texto = texto
        self.color = color

    @abc.abstractmethod
    def dibujar(self):
        pass

    def __str__(self):
        return self.texto + " " + self.color

if __name__ == "__main__":
    fig1 = Figura("circulo1", "red")
    print(fig1)
