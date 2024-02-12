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


class Guia(Persona):
    """
    Implementación de la clase guía
    """
    def __init__(self, nombre="", edad=0, altura=0.0, idiomas=[]):
        # Llamar a la clase Padre:
        Persona.__init__(self, nombre, edad, altura)
        # super().__init__(nombre, edad, altura)
        self.idiomas = idiomas

    def hablarCon(self, otro=None):
        if otro == None:
            super().hablarCon(otro)
        else:
            c1 = set(self.idiomas)
            c2 = set(otro.idiomas)
            comunes = c1 & c2
            if len(comunes) == 0:
                raise ValueError("No coinciden en los idiomas")
            else:
                print(self.nombre,"y",otro.nombre,"pueden hablar en:",comunes)

    def __str__(self):
        return Persona.__str__(self)+" "+";".join(self.idiomas)

def testGuia():
    g1 = Guia("Jorge", 34, 1.8, ['inglés','francés'])
    g2 = Guia("Sara", 45, 1.82, ['alemán','chino'])
    g1.hablarCon(g2)

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
    c = {p1, Persona("Jorge", 56, 1.8), Persona("Raúl", 55, 1.68)}
    L2 = sorted(c)
    print(L2)
    p1.telefono = 917788554
    del p1.__dict__["altura"]
    print(p1.__dict__)
    L3 = [obj.__dict__ for obj in L]
    print(L3)
    # Crear un objeto con el __class__
    p2 = p1.__class__("Jose")
    print(p2)


if __name__ == "__main__":
    #testPersona()
    testGuia()
