"""
POO en Python
"""


class Persona:
    """
    Implementación de la clase persona
    """

    # Att. de clase:
    contador = 0

    def __init__(self, nombre="", edad=0, altura=0.0):
        # Definir e  inicializar att.
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        Persona.contador += 1

    def __str__(self):
        return self.nombre+" "+str(self.edad)+" "+str(self.altura)

    def __del__(self):
        print("Se elimina a ", self.nombre)
        Persona.contador -= 1

if __name__ == '__main__':
    p1 = Persona("Ana",33, 1.8)
    p2 = Persona("Marcos",36, 1.7)
    del(p2)
    print('continua...')
    print(p1)
    print(str(p1))
    print(p1.__str__())

