"""
POO en Python
"""


def crearObjeto(clase, *args):
    return clase(*args)


class Pedido:
    """
    Implementación de la clase pedido
    """

    def __init__(self, idpedido=0, cliente="", importe=0.0, pais=""):
        self.idpedido = idpedido
        self.cliente = cliente
        self.importe = importe
        self.pais = pais

    def __repr__(self):
        return str(self)

    def __str__(self):
        return (
            str(self.idpedido)
            + " "
            + self.cliente
            + " "
            + str(self.importe)
            + " "
            + self.pais
        )

    def __lt__(self, other):
        return self.importe < other.importe

    def __ge__(self, other):
        return self.importe >= other.importe

    def __eq__(self, other):
        # Convertir los valores de los atts. a lista y comparar las dos listas:
        return list(self.__dict__.values()) == list(other.__dict__.values())


class PedidoElectronico(Pedido):

    def __init__(
        self, idpedido=0, cliente="", importe=0.0, pais="", certificado=True, email=""
    ):
        Pedido.__init__(self, idpedido, cliente, importe, pais)
        #super(idpedido, cliente, importe, pais)
        self.certificado = certificado
        self.email = email

    def __str__(self):
        return Pedido.__str__(self) + " " + str(self.certificado) + " " + self.email

def pruebasPedido():
    pedido = Pedido(10248, "ALFKI", 34.99, "España")
    print(pedido)
    # print(str(pedido))
    # print(pedido.__str__())
    pedido.iva = 3.44
    pedido.__dict__["dto"] = 1.5
    print(pedido.__dict__)
    print("La clase: ", pedido.__class__.__name__)

    pedido2 = crearObjeto(Pedido, 10250, "FRTEE", 23.8, "Francia")
    print(pedido2)

    pedido3 = crearObjeto(pedido.__class__, 10260, "FGHAE", 113.9, "Alemania")
    print(pedido3)

    L = [pedido, pedido2, pedido3]
    print(L)
    L.sort(key=lambda ped: ped.pais)
    print(L)
    L.sort()
    print(L)
    if pedido < pedido2:  # if pedido.__lt__(pedido2)
        print(pedido, "es menor")
    else:
        print(pedido2, "es menor")

    if pedido >= pedido2:  # if pedido.__lt__(pedido2)
        print(pedido, "es mayor")
    else:
        print(pedido2, "es mayor")

    pedido4 = crearObjeto(Pedido, 10251, "FRTEE", 23.8, "Francia")
    if pedido4 == pedido2:  # if pedido.__lt__(pedido2)
        print("son iguales")
    else:
        print("son distintos")

    if pedido4 != pedido2:  # if pedido.__lt__(pedido2)
        print("son distintos")
    else:
        print("son iguales")


def pruebasPedidoElectronico():
    ped1 = PedidoElectronico(10248, "ALFKI", 34.99, "España", True, "email")
    print(ped1)

if __name__ == "__main__":
    # pruebasPedido()
    pruebasPedidoElectronico()