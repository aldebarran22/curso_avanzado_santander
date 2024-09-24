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
        if peticion.canal == "whatsapp":
            print("Se envía la petición por WhatsApp")

        elif self.sig != None:
            print('GestorWhatsApp: envía la petición al sig.')
            self.sig.gestionarPeticion(peticion)

        else:
            print('Fin de cadena, no se procesar la petición')
    

class GestorSMS(Gestor):

    def gestionarPeticion(self, peticion):
        if peticion.canal == "sms":
            print("Se envía la petición por sms")

        elif self.sig != None:
            print('GestorSMS: envía la petición al sig.')
            self.sig.gestionarPeticion(peticion)

        else:
            print('Fin de cadena, no se procesar la petición')

class GestorEmail(Gestor):

    def gestionarPeticion(self, peticion):
        if peticion.canal == "email":
            print("Se envía la petición por Email")

        elif self.sig != None:
            print('GestorEmail: envía la petición al sig.')
            self.sig.gestionarPeticion(peticion)

        else:
            print('Fin de cadena, no se procesar la petición') 

if __name__ == "__main__":
    Peticion = namedtuple("Peticion", ['canal','contenido'])
    peticion = Peticion('sms', 'mensaje a enviar')
    #peticion.canal = "email"
    print(peticion.canal)
    print(peticion)
