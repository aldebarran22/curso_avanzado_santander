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
        pass

class DecoradorCerrar(VentanaDecorator):

    def __init__(self, ventana):
        VentanaDecorator.__init__(self, ventana)

    def dibujar(self):
        pass  

class DecoradorAyuda(VentanaDecorator):

    def __init__(self, ventana):
        VentanaDecorator.__init__(self, ventana)

    def dibujar(self):
        pass  
