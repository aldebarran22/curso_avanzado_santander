"""
Seleccionar la factoria de un patrón abstract factory
"""

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
        print(op+1,clase.__name__)
    op = int(input("Opción:"))
    return opciones[op-1]()
    

if __name__ == '__main__':
    fact = seleccionarFactoria(Factoria)
    print(fact.__class__)
