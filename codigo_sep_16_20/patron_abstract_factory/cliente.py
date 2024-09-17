
from Factoria import Factoria
from FactoriaApplet import FactoriaApplet
from FactoriaSamsung import FactoriaSamsung

def seleccionarFactoria():
    L = [c.__name__ for c in Factoria.__subclasses__()]
    print(L)


if __name__ == '__main__':
    seleccionarFactoria()