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
        print(" | ", end="")
        self.ventana.dibujar()
        print(" | ", end=" ")

class BotonCerrarDecorator(VentanaDecorator):

    def dibujar(self):
        print(self.ventana, end="")
        print(" [X]")


class BotonAyudaDecorator(VentanaDecorator):

    def dibujar(self):
        print(self.ventana, end="")
        print(" [?]")   


if __name__ == '__main__':
    v1 = Ventana("Clientes")             
    v2 = BordeDecorator(v1)
    v3 = BordeDecorator(v2)
    v3.dibujar()