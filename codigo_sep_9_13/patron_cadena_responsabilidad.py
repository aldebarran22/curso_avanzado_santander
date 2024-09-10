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
        pass


class ProcesadorEmail(Procesador):

    def procesarPeticion(self, peticion):
        pass


class ProcesadorWhatsApp(Procesador):

    def procesarPeticion(self, peticion):
        pass
