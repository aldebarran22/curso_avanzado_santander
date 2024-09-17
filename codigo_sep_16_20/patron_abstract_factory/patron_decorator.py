"""
Patrón decorator
"""

import abc

class IVentana(abc.ABC):

    @abc.abstractmethod
    def dibujar(self):
        pass

class Ventana(IVentana):

    def __init__(self, titulo):
        self.titulo = titulo

    def dibujar(self):
        print(self.titulo, end="")


class VentanaDecorator(IVentana):

    def __init__(self, ventana):
        self.ventana = ventana

class BordeDecorator(VentanaDecorator):

    def dibujar(self):
        print(" | " + self.ventana.dibujar() + " | ", end=" ")
