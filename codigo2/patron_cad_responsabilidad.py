"""
Patrón Cadena de responsabilidad:
- Trasmitir una petición a través de la cadena
"""
import abc

class Peticion:

    def __init__(self, id, contenido):
        self.id = id
        self.contenido = contenido

    def __str__(self):
        return str(self.id) + " " + str(self.contenido)
    
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
        if peticion.id.upper() == "SMS":
            print("La Petición se envia por SMS: ", peticion.contenido)

        elif self.siguiente == None:
            print('SMS - Fin de cadena')

        else:
            print('SMS pasa la petición al siguiente')
            self.siguiente.trasmitir(peticion)

class GestorEmail(Gestor):

    def __init__(self, siguiente=None):
        Gestor.__init__(self, siguiente)

    def trasmitir(self, peticion):
        if peticion.id.upper() == "EMAIL":
            print("La Petición se envia por EMAIL: ", peticion.contenido)

        elif self.siguiente == None:
            print('EMAIL - Fin de cadena')

        else:
            print('EMAIL pasa la petición al siguiente')
            self.siguiente.trasmitir(peticion)   


class GestorWhatsApp(Gestor):

    def __init__(self, siguiente=None):
        Gestor.__init__(self, siguiente)

    def trasmitir(self, peticion):
        if peticion.id.upper() == "WHATSAPP":
            print("La Petición se envia por WHATSAPP: ", peticion.contenido)

        elif self.siguiente == None:
            print('WHATSAPP - Fin de cadena')

        else:
            print('WHATSAPP pasa la petición al siguiente')
            self.siguiente.trasmitir(peticion)                                 