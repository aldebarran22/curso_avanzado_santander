"""
Implementación del patrón cad. de responsabilidad.
Queremos transmitir un mensaje a un destino y se envía la petición
al primero de la cadena, si no es para él, se transmite al siguiente.
"""

import abc

class Peticion:

    def __init__(self, destino, contenido):
        self.destino = destino
        self.contenido = contenido

class Gestor(abc.ABC):

    def __init__(self, siguiente=None):
        self.siguiente = siguiente

    @abc.abstractmethod
    def trasmitir(self, peticion):
        pass

class GestorSMS(Gestor):

    def __init__(self, siguiente=None):
        Gestor.__init__(self, siguiente)

    def trasmitir(self, peticion):

        if peticion.destino == 'SMS':
            print("Enviar la peticion: ", peticion.contenido,' por SMS')

        elif self.siguiente == None:
            print('Fin de cadena, no se puede realizar la petición')

        else:
            print('SMS trasmite el mensaje al siguiente')
            self.siguiente.trasmitir(peticion)

class GestorEMAIL(Gestor):

    
    def __init__(self, siguiente=None):
        Gestor.__init__(self, siguiente)

    def trasmitir(self, peticion):

        if peticion.destino == 'EMAIL':
            print("Enviar la peticion: ", peticion.contenido,' por EMAIL')

        elif self.siguiente == None:
            print('Fin de cadena, no se puede realizar la petición')

        else:
            print('EMAIL trasmite el mensaje al siguiente')
            self.siguiente.trasmitir(peticion)

class GestorWHATSAPP(Gestor):

    
    def __init__(self, siguiente=None):
        Gestor.__init__(self, siguiente)

    def trasmitir(self, peticion):

        if peticion.destino == 'WHATSAPP':
            print("Enviar la peticion: ", peticion.contenido,' por WHATSAPP')

        elif self.siguiente == None:
            print('Fin de cadena, no se puede realizar la petición')

        else:
            print('WHATSAPP trasmite el mensaje al siguiente')
            self.siguiente.trasmitir(peticion)

if __name__ == '__main__':
    peticion = Peticion("SMS", "Contenido del mensaje")
    cadena = GestorEMAIL(GestorWHATSAPP(GestorSMS()))     
    cadena.trasmitir(peticion)