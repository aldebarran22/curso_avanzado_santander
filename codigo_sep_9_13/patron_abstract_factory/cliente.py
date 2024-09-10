"""
Cliente del abstract factory. 
Muestra un menú con las factorias disponibles
el usuario selecciona una de ellas y crea un teléfono
y una tableta.
"""
from Factoria import Factoria
from FactoriaApplet import FactoriaApplet
from FactoriaSamsung import FactoriaSamsung

def crearFactoria(claseFactoria):

    L = claseFactoria.__subclasses__()
    print('Seleccionar factoría:')
    for pos, clase in enumerate(L):
        print(pos+1, clase.__name__)
    op = int(input("Opción:"))
    return L[op-1]()

if __name__ == '__main__':
    
    #factorias = [c.__name__ for c in Factoria.__subclasses__()]
    #print(factorias)

    fact = crearFactoria(Factoria)
    telefono = fact.createTno()
    tableta = fact.createTablet()

    telefono.llamar()
    tableta.internet()
