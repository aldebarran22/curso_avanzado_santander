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


class VentanaDecorator(IVentana):
    def __init__(self, ventana):
        # Mantiene una referencia a la ventana que decora
        self.ventana = ventana


class BordeDecorator(VentanaDecorator):
    def __init__(self, ventana):
        VentanaDecorator.__init__(self, ventana)

    def dibujar(self):
        print(" | ", end="")
        self.ventana.dibujar()
        print(" | ", end="")


class AyudaDecorator(VentanaDecorator):
    def __init__(self, ventana):
        VentanaDecorator.__init__(self, ventana)

    def dibujar(self):
        self.ventana.dibujar()
        print(" [help] ", end="")


if __name__ == "__main__":
    v1 = Ventana("Clientes")
    v1.dibujar()
    print()

    v2 = BordeDecorator(v1)
    v2.dibujar()
    print()

    v3 = BordeDecorator(AyudaDecorator(Ventana("Aplicación")))
    v3.dibujar()  # | dibujar |
    print()

    v4 = BordeDecorator(BordeDecorator(Ventana("Aplicación")))
    v4.dibujar()  # | dibujar |
    print()

    v5 = Ventana("Clientes")
    for i in range(5):
        v5 = BordeDecorator(v5)
    v5.dibujar()
