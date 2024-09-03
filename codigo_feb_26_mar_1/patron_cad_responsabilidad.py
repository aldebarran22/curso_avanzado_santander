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


class ManejadorEmail(Manejador):

    def __init__(self, siguiente=None):
        Manejador.__init__(self, siguiente)

    def procesarPeticion(self, peticion):
        if peticion.destino == "email":
            print("La peticion se envía por email", peticion.contenido)

        elif not self.siguiente:
            print("Fin de cadena, no se puede trasmitir la petición")
        else:
            # Que procese el siguiente objeto la petición
            print("Email transmite la petición al siguiente")
            self.siguiente.procesarPeticion(peticion)


class ManejadorSMS(Manejador):

    def __init__(self, siguiente=None):
        Manejador.__init__(self, siguiente)

    def procesarPeticion(self, peticion):
        if peticion.destino == "sms":
            print("La peticion se envía por sms", peticion.contenido)

        elif not self.siguiente:
            print("Fin de cadena, no se puede trasmitir la petición")
        else:
            # Que procese el siguiente objeto la petición
            print("SMS transmite la petición al siguiente")
            self.siguiente.procesarPeticion(peticion)


class ManejadorWhatsApp(Manejador):

    def __init__(self, siguiente=None):
        Manejador.__init__(self, siguiente)

    def procesarPeticion(self, peticion):
        if peticion.destino == "WhatsApp":
            print("La peticion se envía por WhatsApp", peticion.contenido)

        elif not self.siguiente:
            print("Fin de cadena, no se puede trasmitir la petición")
        else:
            # Que procese el siguiente objeto la petición
            print("WhatsApp transmite la petición al siguiente")
            self.siguiente.procesarPeticion(peticion)


if __name__ == "__main__":
    peticion = Peticion("video", "contenido del mensaje")
    cad = ManejadorEmail(ManejadorSMS(ManejadorWhatsApp()))
    cad.procesarPeticion(peticion)
