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
        return self.nombre + " " + str(self.edad) + " " + str(self.altura)

    def __repr__(self):
        return str(self)
    """
    def metodo(self):
        print("contador:",self.contador)
    """

    @staticmethod
    def getContador():
        return Persona.contador

    def __del__(self):
        # print("Se elimina a ", self.nombre)
        Persona.contador -= 1


if __name__ == "__main__":
    print("num personas: ", Persona.getContador())
    p1 = Persona("Ana", 33, 1.8)
    p2 = Persona("Marcos", 36, 1.7)
    # del p2 # fuerza la llamada al destructor __del__
    print("Num personas:", p1.contador, Persona.contador)
    print(p1)
    #print(str(p1))
    #print(p1.__str__())
    L = [p1, p2, Persona("Pedro",44,1.9)]
    print(L)
