"""
Patrón Decorator.

Añadir características a una ventana básica
que mantiene sólo el título
Características:
- Borde de la ventana
- Botón de Ayuda
- Botón de cerrar

Y que se puedan combinar.
"""
import abc


class IVentana(abc.ABC):
    @abc.abstractmethod
    def dibujar(self):
        pass


class Ventana(IVentana):
    def __init__(self, titulo="título"):
        self.titulo = titulo

    def dibujar(self):
        print(self.titulo, end="")
