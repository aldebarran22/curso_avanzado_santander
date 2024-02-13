from Factoria import Factoria
from FactoriaApple import FactoriaApple
from FactoriaSamsung import FactoriaSamsung
import sys


def seleccionarFabricante():
    # Mostrar un menú con las factorias disponibles y devolver
    # la factoria creada que haya elegido el cliente.
    L = [c for c in Factoria.__subclasses__()]
    print("MENU")
    for pos, c in enumerate(L):
        print(pos + 1, c.__name__)
    op = int(input("Seleccionar factoria:"))
    return L[op - 1]()

def seleccionarParametro():
    nombreFactoria = "Factoria"+sys.argv[1].capitalize()
    nombre = "{}()".format(nombreFactoria)
    print(nombre)
    clase = eval(nombre)
    return clase

if __name__ == "__main__":
    if len(sys.argv)==1:
        factory = seleccionarFabricante()
    else:
        factory = seleccionarParametro()

    print(factory.__class__)

    tno = factory.createTno()
    tablet = factory.createTablet()

    tno.llamar()
    tablet.internet()
