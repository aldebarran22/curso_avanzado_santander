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

    def __del__(self):
        print("Se elimina a ", self.nombre)
        Persona.contador -= 1

if __name__ == '__main__':
    
