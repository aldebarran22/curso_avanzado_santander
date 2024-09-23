"""
Seleccionar la factoria de un patrón abstract factory
"""

import sys
from Factoria import Factoria
from FactoriaApplet import FactoriaApplet
from FactoriaSamsung import FactoriaSamsung


def seleccionarFactoria(clase_factoria):
    """
    1 Samsung
    2 Apple
    """
    print("Seleccionar Factoria")
    opciones = clase_factoria.__subclasses__()
    for op, clase in enumerate(opciones):
        print(op + 1, clase.__name__)
    op = int(input("Opción:"))
    return opciones[op - 1]()


def seleccionarParam(nombreFact):
    nombreFact = nombreFact.capitalize()
    nombreClass = f"Factoria{nombreFact}"
    nombres = [c.__name__ for c in Factoria.__subclasses__()]
    if nombreClass not in nombres:
        raise ValueError(f"No existe una factoria para {nombreFact}")
    else:
        return eval(nombreClass + "()")


if __name__ == "__main__":
    try:
        if len(sys.argv) == 1:
            fact = seleccionarFactoria(Factoria)
        else:
            fact = seleccionarParam(sys.argv[1])

        #print(fact.__class__)
        telefono = fact.createTno()
        tableta = fact.createTablet()

        telefono.llamar()
        tableta.internet()

    except Exception as e:
        print(e.__class__.__name__, e)
