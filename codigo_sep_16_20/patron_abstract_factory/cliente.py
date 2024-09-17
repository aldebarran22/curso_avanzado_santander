
from Factoria import Factoria
from FactoriaApplet import FactoriaApplet
from FactoriaSamsung import FactoriaSamsung


def seleccionarFactoria():
    L = [c for c in Factoria.__subclasses__()]
    print("MENU")
    for pos, clase in enumerate(L):
        print(pos+1, clase.__name__)
    op = int(input("Opción: "))
    return L[op-1]()

    

if __name__ == '__main__':
    factoria = seleccionarFactoria()
    telefono = factoria.createTno()
    tableta = factoria.createTablet()

    telefono.llamar()
    tableta.internet()