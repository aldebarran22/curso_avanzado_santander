"""
Implementación del patrón: Cadena de Responsabilidad
Montar una cadena de objetos para procesar una petición.
Cada objeto la procesa por un medio distinto:
email, whatsapp, sms ...
"""
import abc


class Peticion:
    def __init__(self, destino, contenido):
        self.destino = destino
        self.contenido = contenido


class Manejador(abc.ABC):
    def __init__(self, siguiente=None):
        self.siguiente = siguiente  # El siguiente de la cadena

    @abc.abstractmethod
    def procesarPeticion(self, peticion):
        pass


class Email(Manejador):
    pass


class SMS(Manejador):
    pass


class WhatsApp(Manejador):
    pass
