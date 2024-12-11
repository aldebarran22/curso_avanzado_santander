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

    def trasmitir(self, peticion):

        if peticion.destino == 'SMS':
            print("Enviar la peticion: ", peticion.contenido,' por SMS')

        elif self.siguiente != None:
            print('Fin de cadena, no se puede realizar la petición')

        else:
            self.siguiente.trasmitir(peticion)

class GestorEMAIL(Gestor):

    def trasmitir(self, peticion):

        if peticion.destino == 'SMS':
            print("Enviar la peticion: ", peticion.contenido,' por SMS')

        elif self.siguiente != None:
            print('Fin de cadena, no se puede realizar la petición')

        else:
            self.siguiente.trasmitir(peticion)