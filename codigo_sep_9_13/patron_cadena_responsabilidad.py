"""
Cadena de responsabilidad. Transmitir un mensaje
a través de la cadena sin conocer quien es
el objeto que procesará la petición.
El mensaje se transfiere por la cadena de 
una forma automática.
"""

import abc

class Peticion:
    def __init__(self, destino, contenido):
        self.destino = destino # SMS, EMAIL, WHATSAPP
        self.contenido = contenido

class Procesador(abc.ABC):

    def __init__(self, siguiente=None):
        self.siguiente = siguiente

    @abc.abstractmethod
    def procesarPeticion(self, peticion):
        pass


class ProcesadorSMS(Procesador):

    def procesarPeticion(self, peticion):
        if peticion.destino.lower() == 'sms':
            print('La petición se enviar por SMS')

        elif self.siguiente != None:
            print('SMS envía al siguiente la petición')
            self.siguiente.procesarPeticion(peticion)

        else:
            print('SMS fin de cadena, no se puede procesar la petición')


class ProcesadorEmail(Procesador):

    def procesarPeticion(self, peticion):
        if peticion.destino.lower() == 'email':
            print('La petición se enviar por email')

        elif self.siguiente != None:
            print('EMAIL envía al siguiente la petición')
            self.siguiente.procesarPeticion(peticion)

        else:
            print('EMAIL fin de cadena, no se puede procesar la petición')


class ProcesadorWhatsApp(Procesador):

    def procesarPeticion(self, peticion):
        if peticion.destino.lower() == 'whatsapp':
            print('La petición se enviar por WhatsApp')

        elif self.siguiente != None:
            print('WhatsApp envía al siguiente la petición')
            self.siguiente.procesarPeticion(peticion)

        else:
            print('WhatsApp fin de cadena, no se puede procesar la petición')



if __name__=='__main__':
    peticion = Peticion("SMS", "Contenido del mensaje a enviar")

    cad = ProcesadorSMS(ProcesadorEmail(ProcesadorWhatsApp()))
    cad.procesarPeticion(peticion)


