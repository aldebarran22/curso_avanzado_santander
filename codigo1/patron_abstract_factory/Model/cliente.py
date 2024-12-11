
from Factoria import Factoria
from Samsung import Samsung
from Applet import Applet

def menu(opciones):
    print('Menu:')
    for pos, c in enumerate(opciones):
        print(pos+1, c.__name__)
    op = int(input('Seleccionar factoria: '))
    return opciones[op-1]()

if __name__=='__main__':
    clases = [c.__name__ for c in Factoria.__subclasses__()]
    print(clases)

    factoria = menu(Factoria.__subclasses__())
    print(factoria.__class__.__name__)

