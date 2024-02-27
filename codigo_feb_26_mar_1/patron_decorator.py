"""
Patrón decorator
"""

import abc


class IVentana(abc.ABC):

    @abc.abstractmethod
    def dibujar(self):
        pass


class Ventana(IVentana):

    def __init__(self, titulo=""):
        self.titulo = titulo

    def dibujar(self):
        print(self.titulo, end=" ")


class VentanaDecorator(IVentana):

    def __init__(self, ventana):
        self.ventana = ventana


class BordeDecorator(VentanaDecorator):

    def __init__(self, ventana):
        VentanaDecorator.__init__(self, ventana)

    def dibujar(self):
        print("|", end=" ")
        self.ventana.dibujar()
        print("|", end=" ")


class BotonCerrarDecorator(VentanaDecorator):

    def __init__(self, ventana):
        VentanaDecorator.__init__(self, ventana)

    def dibujar(self):
        print("[x]", end=" ")
        self.ventana.dibujar()


if __name__ == "__main__":
    v1 = BordeDecorator(Ventana("Ventana con Borde"))
    v1.dibujar()
    print()

    v2 = BordeDecorator(BordeDecorator(Ventana("Ventana con 2 Bordes")))
    v2.dibujar()
    print()

    v3 = BordeDecorator(
        BotonCerrarDecorator(Ventana("Ventana con Borde y boton cerrar"))
    )
    v3.dibujar()
    print()
