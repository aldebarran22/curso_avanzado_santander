"""
Patrones estructurales: Decorator
"""

import abc


class IVentana(abc.ABC):

    @abc.abstractmethod
    def dibujar(self):
        pass


class Ventana(IVentana):

    def __init__(self, titulo="ventana"):
        self.titulo = titulo

    def dibujar(self):
        print(self.titulo, end=" ")


class VentanaDecorator(IVentana):

    def __init__(self, ventana):
        self.ventana = ventana


class DecoradorBorde(VentanaDecorator):

    def __init__(self, ventana):
        VentanaDecorator.__init__(self, ventana)

    def dibujar(self):
        print("|", end=" ")
        self.ventana.dibujar()
        print("|", end=" ")


class DecoradorCerrar(VentanaDecorator):

    def __init__(self, ventana):
        VentanaDecorator.__init__(self, ventana)

    def dibujar(self):
        self.ventana.dibujar()
        print("X", end=" ")


class DecoradorAyuda(VentanaDecorator):

    def __init__(self, ventana):
        VentanaDecorator.__init__(self, ventana)

    def dibujar(self):
        print("[Ayuda]", end=" ")
        self.ventana.dibujar()


if __name__ == "__main__":
    # Ventana con borde:
    # |Ventana con borde|
    v1 = DecoradorBorde(Ventana("Ventana con borde"))
    v1.dibujar()
    print()

    # ||Ventana con 2 bordes||
    v3 = DecoradorBorde(DecoradorBorde(Ventana("Ventana con 2 bordes")))
    v3.dibujar()
    print()

    # Ventana con todo:
    # |Ventana con todo[Ayuda] X|
    v2 = DecoradorBorde(DecoradorAyuda(DecoradorCerrar(Ventana("Ventana con todo"))))
    v2.dibujar()
    print()
