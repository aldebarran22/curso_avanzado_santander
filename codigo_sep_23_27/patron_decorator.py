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

