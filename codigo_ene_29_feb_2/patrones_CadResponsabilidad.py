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
    def __init__(self, siguiente=None):
        Manejador.__init__(self, siguiente)

    def procesarPeticion(self, peticion):
        if peticion.destino == "email":
            print("Enviar email con: ", peticion.contenido)

        elif self.siguiente != None:
            print("Email: Transmitir la petición al siguiente.")
            self.siguiente.procesarPeticion(peticion)
        else:
            print("Fin de cadena, no se puede procesar")


class SMS(Manejador):
    def __init__(self, siguiente=None):
        Manejador.__init__(self, siguiente)

    def procesarPeticion(self, peticion):
        if peticion.destino == "sms":
            print("Enviar SMS con: ", peticion.contenido)

        elif self.siguiente != None:
            print("SMS: Transmitir la petición al siguiente.")
            self.siguiente.procesarPeticion(peticion)
        else:
            print("Fin de cadena, no se puede procesar")


class WhatsApp(Manejador):
    def __init__(self, siguiente=None):
        Manejador.__init__(self, siguiente)

    def procesarPeticion(self, peticion):
        if peticion.destino == "whatsapp":
            print("Enviar whatsapp con: ", peticion.contenido)

        elif self.siguiente != None:
            print("WhatsApp: Transmitir la petición al siguiente.")
            self.siguiente.procesarPeticion(peticion)
        else:
            print("Fin de cadena, no se puede procesar")


if __name__ == "__main__":
    peticion = Peticion("telegram", "Contenido del mensaje")

    cadenaResp = Email(WhatsApp(SMS()))
    cadenaResp.procesarPeticion(peticion)
