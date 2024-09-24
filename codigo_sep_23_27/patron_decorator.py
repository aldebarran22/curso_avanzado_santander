"""
Patrón decorator:
Crear una ventana y añadirla nuevas característica
mediante decoradores.
"""

import abc

class IVentana(abc.ABC):

    @abc.abstractmethod
    def dibujar(self):
        pass

class Ventana(IVentana):

    def __init__(self, titulo="un titulo"):
        self.titulo = titulo

    def dibujar(self):
        print(self.titulo, end='')


class VentanaDecorador(IVentana):

    def __init__(self, ventana):
        self.ventana = ventana

class VentanaBorderDecorator(VentanaDecorador):

    def dibujar(self):
        print("|", end="")
        self.ventana.dibujar()
        print("|", end="")

class VentanaAyudaDecorator(VentanaDecorador):

    def dibujar(self):
        print("[Botón]", end="")
        self.ventana.dibujar()

if __name__ == '__main__':
    v1 = Ventana("CLIENTES")
    v1.dibujar()

    v2 = VentanaBorderDecorator(v1)
    v2.dibujar()

    v3 = VentanaBorderDecorator(VentanaAyudaDecorator(Ventana("CLIENTES")))
    v3.dibujar()