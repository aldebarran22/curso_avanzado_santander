from Factoria import Factoria
from FactoriaApple import FactoriaApple
from FactoriaSamsung import FactoriaSamsung


def seleccionarFabricante():
    # Mostrar un menú con las factorias disponibles y devolver
    # la factoria creada que haya elegido el cliente.
    L = [c for c in Factoria.__subclasses__()]
    print("MENU")
    for pos, c in enumerate(L):
        print(pos + 1, c.__name__)
    op = int(input("Seleccionar factoria:"))
    return L[op - 1]()


if __name__ == "__main__":
    factory = seleccionarFabricante()
    print(factory.__class__)

    tno = factory.createTno()
    tablet = factory.createTablet()

    tno.llamar()
    tablet.internet()
