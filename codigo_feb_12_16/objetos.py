"""
POO en Python
"""


class Persona:
    """
    Implementar la clase Persona
    """

    def __init__(self, nombre="", edad=0, altura=0.0):
        # Definición de atributos:
        self.nombre = nombre
        self.edad = edad
        self.altura = altura

    def cumple(self):
        self.edad += 1

    def hablarCon(self, otro=None):
        if not otro:
            print(self.nombre, "está hablando solo")
        else:
            # f-string
            print(f"{self.nombre} y {otro.nombre} están hablando")

    def __str__(self):
        return self.nombre + " " + str(self.edad) + " " + str(self.altura)

    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        return self.edad < other.edad

    def __del__(self):
        # print("se borra a ", self.nombre)
        pass


def testPersona():
    p1 = Persona("Ana", 23, 1.77)
    print(p1)
    # print(str(p1))
    # print(p1.__str__())
    L = [p1, Persona("Jorge", 44, 1.8), Persona("Raúl", 55, 1.68)]
    print(L)
    L.sort(key=lambda obj: obj.nombre, reverse=True)
    print(L)
    L.sort()
    print(L)


if __name__ == "__main__":
    testPersona()
