"""
Patrón de comportamiento: Cadena de Responsabilidad
Transmitir una petición a través de la cadena
Se la envíamos al primer objeto y si es para él
la trata, si no la envía al siguiente de la cadena.
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
