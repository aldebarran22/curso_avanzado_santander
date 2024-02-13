from Factoria import Factoria
from FactoriaApple import FactoriaApple
from FactoriaSamsung import FactoriaSamsung


def seleccionarFabricante():
    L = Factoria.__subclasses__()
    print(L)


if __name__ == "__main__":
    factory = seleccionarFabricante()
    """
    tno = factory.createTno()
    tablet = factory.createTablet()

    tno.llamar()
    tablet.internet()
    """
