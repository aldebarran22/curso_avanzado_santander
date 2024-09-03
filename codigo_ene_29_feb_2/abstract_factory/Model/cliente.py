"""
Utiliza el patrón abstract factory
y selecciona la factoria a través de la línea de 
comandos.

python cliente.py Samsung | Apple
"""
from Factoria import Factoria
from FactoriaApple import FactoriaApple
from FactoriaSamsung import FactoriaSamsung


def menu(L):
    print("MENU")
    for pos, c in enumerate(L):
        print(pos + 1, c.__name__)
    op = int(input("Seleccionar factoria: "))
    return L[op - 1]()


if __name__ == "__main__":
    L = Factoria.__subclasses__()
    factoria = menu(L)
    # print(factoria.__class__)
    telefono = factoria.createTno()
    tableta = factoria.createTablet()

    telefono.llamar()
    tableta.internet()
