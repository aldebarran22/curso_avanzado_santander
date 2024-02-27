"""
Patrón decorator
"""

import abc

class IVentana(abc.ABC):

    @abc.abstractmethod
    def dibujar(self):
        pass

class Ventana(IVentana):

    def __init__(self,titulo=""):
        self.titulo=titulo

    def dibujar(self):
        print(self.titulo,end=" ")

class VentanaDecorator(IVentana):

    def __init__(self, ventana):
        self.ventana=ventana

class BordeDecorator(VentanaDecorator):

    def __init__(self, ventana):
        VentanaDecorator.__init__(self,ventana)

    def dibujar(self):
        pass

class BotonCerrarDecorator(VentanaDecorator):

    def __init__(self, ventana):
        VentanaDecorator.__init__(self,ventana)

    def dibujar(self):
        pass

if __name__ == '__main__':
    v1 = BordeDecorator(Ventana("Ventana con Borde"))
    v1.dibujar()
    print()

    v2 = BordeDecorator(BordeDecorator(Ventana("Ventana con Borde")))
    v2.dibujar()
    print()
    