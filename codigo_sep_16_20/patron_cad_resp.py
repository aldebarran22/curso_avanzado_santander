"""
Patrón cadena de responsabilidad
"""

from collections import namedtuple
import abc

class Manejador(abc.ABC):

    def __init__(self,sig=None):
        self.sig = sig

    @abc.abstractmethod
    def gestionarPeticion(self, peticion):
        pass

class ManejadorSMS(Manejador):
    
    def gestionarPeticion(self, peticion):
        if (peticion.tipo == 'SMS'):
            print('SMS : '+peticion.contenido)

        elif self.sig != None:
            print('SMS transmite al siguiente')
            self.sig.gestionarPeticion(peticion)

        else:
            print('SMS : no puede gestionar la petición')

class ManejadorEmail(Manejador):
    
    def gestionarPeticion(self, peticion):
        if (peticion.tipo == 'Email'):
            print('Email : '+peticion.contenido)

        elif self.sig != None:
            print('Email transmite al siguiente')
            self.sig.gestionarPeticion(peticion)

        else:
            print('Email no se puede gestionar la petición')

class ManejadorWhatsApp(Manejador):
    
    def gestionarPeticion(self, peticion):
        if (peticion.tipo == 'WhatsApp'):
            print('WhatsApp : '+peticion.contenido)

        elif self.sig != None:
            print('WhatsApp transmite al siguiente')
            self.sig.gestionarPeticion(peticion)

        else:
            print('WhatsApp : no se puede gestionar la petición')


if __name__ == '__main__':
    Peticion = namedtuple('Peticion',['tipo','contenido'])
    ped = Peticion("VideoConferencia", "Contenido del mensaje")
    print(ped)
    print(ped.tipo)

    cadena = ManejadorWhatsApp(ManejadorEmail(ManejadorSMS()))
    cadena.gestionarPeticion(ped)
