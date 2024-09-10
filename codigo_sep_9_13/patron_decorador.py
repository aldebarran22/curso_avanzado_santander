"""
Patrón decorator:
Partir de una ventana básica (con el título) y la vamos decorando
con distintos objetos que añaden una funcionalidad nueva.
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
        print(self.titulo, end="")


class VentanaDecorator(IVentana):

    def __init__(self, ventana):
        self.ventana = ventana


class DecoratorBorde(VentanaDecorator):

    def dibujar(self):
        print(" | ", end="")
        self.ventana.dibujar()
        print(" | ", end="")


class DecoratorBotonAyuda(VentanaDecorator):
    
    def dibujar(self):
        print(" [?] ", end="")
        self.ventana.dibujar()


class DecoratorBotonCerrar(VentanaDecorator):
    
    def dibujar(self):
        print(" [x] ", end="")
        self.ventana.dibujar()


if __name__ == "__main__":
    v1 = Ventana("Titulo de la ventana")
    v1.dibujar()
    print()

    v2 = DecoratorBorde(v1)
    v2.dibujar()
    print()

    v3 = DecoratorBorde(DecoratorBorde(v1))
    v3.dibujar()
    print()

    v4 = DecoratorBorde(DecoratorBotonAyuda(Ventana("Titulo")))
    v4.dibujar()
    print()
