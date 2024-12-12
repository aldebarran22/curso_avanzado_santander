"""
Seleccionar de forma dinámica la factoria con la que vamos
a trabajar.
"""

from Factoria import Factoria
from Applet import Applet
from Samsung import Samsung


def seleccionarFactoria(clases):
    print('Seleccionar familia de productos:')
    for pos, clase in enumerate(clases, start=1):
        print(pos, clase.__name__)
    op = int(input('Número de factoria:'))
    return clases[op-1]()


if __name__ == '__main__':
    factoria = seleccionarFactoria(Factoria.__subclasses__())
    print("Familia seleccionada: ", factoria.__class__.__name__)
    telefono = factoria.crearTno()
    tableta = factoria.crearTablet()

    telefono.llamar()
    tableta.internet()