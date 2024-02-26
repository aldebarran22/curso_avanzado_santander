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

    def __lt__(self, other):
        return self.edad < other.edad

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

def testPersona():
    print("num personas: ", Persona.getContador())
    p1 = Persona("Ana", 33, 1.8)
    p2 = Persona("Marcos", 36, 1.7)
    # del p2 # fuerza la llamada al destructor __del__
    print("Num personas:", p1.contador, Persona.contador)
    print(p1)
    # print(str(p1))
    # print(p1.__str__())
    L = [p1, p2, Persona("Pedro", 44, 1.9)]
    L.sort(key=lambda obj: obj.altura, reverse=True)
    print(L)
    L.sort()  # Utiliza el operador < __lt__  (less than)
    print(L)
    #if p1.__lt__(p2):
    if p1 < p2:
        print(p1.nombre, "es menor que", p2.nombre)
    else:
        print(p2.nombre, "es menor que", p1.nombre)

    # Convertir a json
    Ljson = [obj.__dict__ for obj in L]
    print(Ljson)
    p1.__dict__['tno'] = 914456677
    print(p1.tno)
    p1.movil = 656445533
    print(p1.__dict__)

    
def crearObjetos():
    p1 = Persona("Ana", 33, 1.8)
    print('La clase:',p1.__class__.__name__)

    # Crear un objeto con el class:
    p2 = p1.__class__("Juan",23,1.8)
    print(p2)

    # Crear un objeto con una cadena:
    cad = "{}({},{},{})".format("Persona", "'Sara'",44,1.88)
    print(cad)
    p3 = eval(cad)
    print(p3)

if __name__ == "__main__":
    #testPersona()
    crearObjetos()