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
    
class Circulo(Figura):

    def __init__(self, texto="", color="black", radio=5.0):
        Figura.__init__(self, texto, color)
        self.radio = radio 

    def dibujar(self):
        print('Circulo de radio: ', self.radio, " ", str(self))


if __name__ == "__main__":
    fig1 = Circulo("circulo1", "red")
    fig1.dibujar()
