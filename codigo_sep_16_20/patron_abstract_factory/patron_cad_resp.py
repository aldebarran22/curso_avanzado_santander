"""
Patrón cadena de responsabilidad
"""

from collections import namedtuple
import abc

class Manejador(abc.ABC):

    def __init__(self,sig=None):
        self.sig = sig

    @abc.abstractmethod
    def gestionarPeticion(self):
        pass

if __name__ == '__main__':
    Peticion = namedtuple('Peticion',['tipo','contenido'])
    ped = Peticion("SMS", "Contenido del mensaje")
    print(ped)
    print(ped.tipo)
