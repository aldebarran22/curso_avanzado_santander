"""
Implementación del patrón cad. resp. 
Para enviar una petición por 3 tipos de canales:
sms, whatsapp, email
"""

from collections import namedtuple
import abc

class Gestor(abc.ABC):

    def __init__(self,sig=None):
        self.sig = sig

    @abc.abstractmethod
    def gestionarPeticion(self, peticion):
        pass

class GestorWhatsApp(Gestor):

    def gestionarPeticion(self, peticion):
        pass

class GestorSMS(Gestor):

    def gestionarPeticion(self, peticion):
        pass

class GestorEmail(Gestor):

    def gestionarPeticion(self, peticion):
        pass    

if __name__ == "__main__":
    Peticion = namedtuple("Peticion", ['canal','contenido'])
    peticion = Peticion('sms', 'mensaje a enviar')
    #peticion.canal = "email"
    print(peticion.canal)
    print(peticion)
