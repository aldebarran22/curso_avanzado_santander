"""
Seleccionar la factoria del AbstractFactory
a partir de un menú dinámico o con la linea de comandos
"""

import sys
from Factoria import Factoria
from FactoriaApple import FactoriaApple
from FactoriaSamsung import FactoriaSamsung


def menu(L):
    pass


if __name__ == "__main__":
    L = [c.__name__ for c in Factoria.__subclasses__()]
    if len(sys.argv) >= 2:
        nombreFact = "Factoria" + sys.argv[1].capitalize()
        if nombreFact not in L:
            print("Factoria no soportada")
            exit()
        else:
            nombreFact += "()"
            factoria = eval(nombreFact)

    else:
        # lanzar el menu:
        factoria = menu(L)

    telefono = factoria.createTno()
    tableta = factoria.createTablet()

    telefono.llamar()
    tableta.internet()
